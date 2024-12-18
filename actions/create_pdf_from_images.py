import img2pdf
from PIL import Image
import os

# https://pypi.org/project/img2pdf/

image_path: str = './../images_origin/'
image_name: str = '1a90'
image_extension: str = '.png'
img_read = '{}{}{}'.format(image_path, image_name, image_extension)
pdf_path = '{}{}.pdf'.format(image_path, image_name)


# opening from filename
with open(pdf_path, 'wb') as f:
	f.write(img2pdf.convert(img_read))