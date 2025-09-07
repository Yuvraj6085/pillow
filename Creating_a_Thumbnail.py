from PIL import Image
image = Image.open(r"anu.jpg")
MAX_SIZE = (100, 100)
image.thumbnail(MAX_SIZE)

image.show()