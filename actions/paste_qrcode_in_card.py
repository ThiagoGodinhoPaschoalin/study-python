import cv2, numpy
from datetime import datetime, timezone
from qrcode import QRCode, constants

image_path: str = './../images_origin/'
image_name: str = '1a90'
image_extension: str = '.png'
img_read = '{}{}{}'.format(image_path, image_name, image_extension)
x: int = 2100
y: int = 2970
qrcode_data = 'dados do usuário e avaliação aqui...'

image: cv2.Mat = cv2.imread(img_read)
image = cv2.resize(image, (x, y))

qr = QRCode(version=1, error_correction=constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(qrcode_data)
qr.make(fit=True)
qrcode_image = qr.make_image(back_color=(255, 255, 255), fill_color=(0, 0, 0))
#qrcode_image.save(f'{image_path}qrcode.png')
#qrcode_image: cv2.Mat = cv2.imread(f'{image_path}qrcode.png')
#qrcode_image = cv2.resize(qrcode_image, (560, 560))
qrcode_image = numpy.array(qrcode_image, dtype=numpy.uint8)# Convert RGB to BGR
qrcode_image = cv2.resize(qrcode_image, (600, 600))
h, w = qrcode_image.shape[:2]
image[125:125+h, 1375:1375+w] = qrcode_image

datenow = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")
cv2.imwrite('{}{}_{}x{}_{}{}'.format(image_path, image_name, x, y, datenow, image_extension), image)
