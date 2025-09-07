from PIL import Image
image = Image.open(r"priya.jpg")
image.load()
r, g, b, = image.split()
im1 = Image.merge('RGB', (g, b, r))
im1.show()


