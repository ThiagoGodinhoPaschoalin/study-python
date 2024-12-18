import cv2, numpy
from PIL import ImageFont, ImageDraw, Image

# Create black mask using Numpy and convert from BGR (OpenCV) to RGB (PIL)
# image = cv2.imread('1.png') # If you were using an actual image
# (height, width, _) = image.shape

''' v1:
image = numpy.zeros((250, 1000, 3), dtype=numpy.uint8)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pil_image = Image.fromarray(image)
'''
pil_image = Image.new(mode="RGBA", size=(1000,250), color="pink")

# Draw non-ascii text onto image
font = ImageFont.truetype("__arial.ttf", 35)
draw = ImageDraw.Draw(pil_image)
draw.text((0, 0), "Avaliação: Aluná", font=font, fill="black")
draw.text((0, 50), "Avaliação: Aluná", font=font)
draw.text((0, 100), "Avaliação: Aluná", font=font)
draw.text((0, 150), "Avaliação: Aluná", font=font)
draw.text((0, 200), "Avaliação: Aluná", font=font)

# Convert back to Numpy array and switch back from RGB to BGR
image = numpy.asarray(pil_image)
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imshow('image', image)
cv2.waitKey()