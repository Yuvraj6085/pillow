from PIL import Image
img=Image.open('tamana.jpg')
img1=img.transpose(method=Image.FLIP_TOP_BOTTOM)
img.show()
img1.show()

# close window
img1.close()
img.close()