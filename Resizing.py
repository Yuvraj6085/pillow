from PIL import Image
img=Image.open('tamana.jpg')
width,height=img.size
left=4
top = height / 5
right = 154
bottom = 3 * height / 5
im1 = img.crop((left, top, right, bottom))
newsize = (300, 300)
im1 = im1.resize(newsize)
im1.show()