def generate_numeric_wordlist(output_file, start, end):
    with open(output_file, "w") as f:
        for i in range(start, end + 1):
            f.write(str(i) + "\n")

generate_numeric_wordlist("numeric_wordlist.txt", 0, 9999999)
print("Wordlist generated as numeric_wordlist.txt")