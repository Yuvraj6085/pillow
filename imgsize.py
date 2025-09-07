from PIL import Image
import PIL 
img=Image.open('tamana.jpg')
# size img 
print(img.size)
# image formate 
print(img.format)

# Getting Color mode of the image
print(img.mode)