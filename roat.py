from PIL import Image
import PIL 
img=Image.open('tamana.jpg')

# Rotating the Image
img=img.rotate(45,PIL.Image.NEAREST,expand=1)
img.show()