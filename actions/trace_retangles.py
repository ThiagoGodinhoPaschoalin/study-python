import cv2, numpy

class Point:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

class Retangle:
  def __init__(self, contour: cv2.typing.MatLike):
    self.__extractions(contour)

  def __extractions(self, contour: cv2.typing.MatLike):
    self.contour: cv2.typing.MatLike = contour
    coordinates = [tuple(pair[0]) for pair in contour]
    self.x_final: int = max(coordinates, key=lambda coord: coord[0])[0]
    self.x_initial: int = min(coordinates, key=lambda coord: coord[0])[0]
    self.y_final: int = max(coordinates, key=lambda coord: coord[1])[1]
    self.y_initial: int = min(coordinates, key=lambda coord: coord[1])[1]
    self.p0 = Point(self.x_initial, self.y_initial)
    self.pF = Point(self.x_final, self.y_final)
    self.width: int = self.x_final - self.x_initial
    self.height: int = self.y_final - self.y_initial
    self.set_corner_points()
  
  def set_corner_points(self) -> numpy.float32:
    self.corner_points = Retangle.generate_corner_points(self.contour)

  @staticmethod
  def mount_corner_point(x0: int, y0: int, xF: int, yF: int) -> numpy.float32:
    return numpy.float32([ [x0, y0], [xF, y0], [x0, yF], [xF, yF] ])
  
  @staticmethod
  def generate_corner_points(contour: cv2.typing.MatLike) -> numpy.float32:
    perimeter = cv2.arcLength(contour, True)
    approximation = cv2.approxPolyDP(contour, .02 * perimeter, True)
    #sort the corner points
    corner_point = approximation.reshape((4, 2))
    new_points = numpy.zeros((4, 1, 2), numpy.int32)
    add = corner_point.sum(1)
    new_points[0] = corner_point[numpy.argmin(add)]
    new_points[3] = corner_point[numpy.argmax(add)]
    diff = numpy.diff(corner_point, axis=1)
    new_points[1] = corner_point[numpy.argmin(diff)]
    new_points[2] = corner_point[numpy.argmax(diff)]
    return numpy.float32(new_points)





def pontos_do_quadrado(contorno):
  coordenadas = [tuple(pair[0]) for pair in contorno]
  x_max = max(coordenadas, key=lambda coord: coord[0])[0]
  x_min = min(coordenadas, key=lambda coord: coord[0])[0]
  y_max = max(coordenadas, key=lambda coord: coord[1])[1]
  y_min = min(coordenadas, key=lambda coord: coord[1])[1]
  return { 'hf': y_max, 'hi': y_min, 'wf': x_max, 'wi': x_min, 'y': y_max - y_min, 'x': x_max - x_min }
  


image_path: str = './../images/IMG_ESCOLA_01/'
image_name: str = 'IMG_ESCOLA_01'
image_name: str = 'scale_IMG_ESCOLA_01'
image_name: str = 'rotate_IMG_ESCOLA_01'
image_extension: str = '.jpg'
img_read = '{}{}{}'.format(image_path, image_name, image_extension)
x: int = 2100
y: int = 2970

image: cv2.Mat = cv2.imread(img_read)

cv2.imshow("original", image)
cv2.waitKey(0)

image = cv2.resize(image, (x, y))

# obter contornos
img_copy = image.copy()
img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
img_copy = cv2.GaussianBlur(img_copy, (5, 5), 1)
img_copy = cv2.Canny(img_copy, 10, 50)
contours, _ = cv2.findContours(img_copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# obter retangulos
rectangle_contours = []
for contour in contours:
  area = cv2.contourArea(contour)
  if area > 50:
    # obter perimetro e aproximação
    perimeter = cv2.arcLength(contour, True)
    approximation = cv2.approxPolyDP(contour, .02 * perimeter, True)
    # Quatro pontos, é um quadrado/retangulo 
    if len(approximation) == 4:
      rectangle_contours.append(contour)

# ordenar retangulos por area
rectangle_contours = sorted(rectangle_contours, key=cv2.contourArea, reverse=True)

# "questions": { "x": 222, "y": 937, "width": 1655, "height": 1820 }, chunk=(1820, 1655)
respostas = rectangle_contours[0]
delta = pontos_do_quadrado(respostas)
canvas = image[delta['hi']:delta['hf'], delta['wi']:delta['wf']]
cv2.imshow("respostas", canvas)
cv2.waitKey(0)

'''
qrcode = rectangle_contours[1]
delta = pontos_do_quadrado(qrcode)
canvas = image[delta['hi']:delta['hf'], delta['wi']:delta['wf']]
cv2.imshow("qrcode", canvas)
cv2.waitKey(0)


eletiva = rectangle_contours[2]
delta = pontos_do_quadrado(eletiva)
canvas = image[delta['hi']:delta['hf'], delta['wi']:delta['wf']]
cv2.imshow("eletiva", canvas)
cv2.waitKey(0)
'''


'''
cv2.drawContours(image, [respostas], 0, (255, 0, 0), 2)
cv2.drawContours(image, [qrcode], 0, (0, 255, 0), 2)
cv2.drawContours(image, [eletiva], 0, (0, 0, 255), 2)
cv2.imshow('Image', image)
cv2.waitKey(0)
'''

#obter respostas
height, width = (1820, 1655) # Tamanho original da folha de respostas

retangulo: Retangle = Retangle( rectangle_contours[0] )
points_one = retangulo.corner_points
points_two = Retangle.mount_corner_point(0, 0, width, height )
matrix = cv2.getPerspectiveTransform(points_one, points_two)
perspective = cv2.warpPerspective(image, matrix, (width, height))

cv2.imshow("warpPerspective", perspective)
cv2.waitKey(0)
