from PIL import Image, ImageFont, ImageDraw
image = Image.open("anu.jpg")
watermark_image = image.copy()
draw = ImageDraw.Draw(watermark_image)
font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 50)
draw.text((10, 10), "Vinit", fill=(255, 255, 255), font=font)
watermark_image.show()
