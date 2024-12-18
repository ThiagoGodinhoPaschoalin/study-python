import cv2
from datetime import datetime, timezone


image_path: str = './../images_origin/'
image_name: str = '1a90'
image_extension: str = '.png'
img_read = '{}{}{}'.format(image_path, image_name, image_extension)
x: int = 2100
y: int = 2970

image: cv2.Mat = cv2.imread('{}{}{}'.format(image_path, image_name, image_extension))
image = cv2.resize(image, (x, y))
datenow = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")
cv2.imwrite('{}{}_{}x{}_{}{}'.format(image_path, image_name, x, y, datenow, image_extension), image)