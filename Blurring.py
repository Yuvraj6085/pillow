from PIL import Image, ImageFilter
im = Image.open(r"anu.jpg")
im1 = im.filter(ImageFilter.GaussianBlur(4))
im1.show()