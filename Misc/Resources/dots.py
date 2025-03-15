from PIL import Image, ImageChops

# Open the GIF file
im = Image.open("dots.gif")
frames = []
try:
    while True:
        frame = im.convert("RGBA")
        frames.append(frame.copy())
        im.seek(im.tell()+1)
except EOFError:
    pass

# Create a blank canvas the same size as the frames
composite = Image.new("RGBA", frames[0].size, (0,0,0,0))
for frame in frames:
    composite = ImageChops.lighter(composite, frame)

composite.save("composite.png")