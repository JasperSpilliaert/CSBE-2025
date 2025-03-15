import subprocess
import zipfile
import os

def crack_zip_with_john(zip_file, wordlist="numeric_wordlist.txt"):
    hash_file = f"{zip_file}.hash"
    try:
        with open(hash_file, "w") as hf:
            subprocess.run(["zip2john", zip_file], stdout=hf, check=True)
        
        subprocess.run(["john", f"--wordlist={wordlist}", hash_file], check=True)
        
        result = subprocess.run(["john", "--show", hash_file], capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        
        pwd = None
        for line in output.splitlines():
            if line.startswith(zip_file + ":"):
                parts = line.split(":")
                if len(parts) >= 2:
                    pwd = parts[1]
                    break
        
        if pwd is None:
            print(f"Password not found for {zip_file}")
            return None, None
        
        with zipfile.ZipFile(zip_file) as z:
            with z.open("character.txt", pwd=pwd.encode('utf-8')) as f:
                content = f.read().decode('utf-8').strip()
        return content, pwd
    except subprocess.CalledProcessError as e:
        print(f"Error processing {zip_file}: {e}")
        return None, None
    except Exception as e:
        print(f"Unexpected error with {zip_file}: {e}")
        return None, None
    finally:
        if os.path.exists(hash_file):
            os.remove(hash_file)

flag_chars = {}

for i in range(19):
    zip_name = f"{i}.zip"
    char, pwd_used = crack_zip_with_john(zip_name)
    if char is None:
        print(f"Failed to crack {zip_name}")
    else:
        flag_chars[i] = char
        print(f"Cracked {zip_name} with password '{pwd_used}', character: '{char}'")

flag = ''.join(flag_chars[i] for i in sorted(flag_chars.keys()) if i in flag_chars)
print("\nFlag:", flag)
