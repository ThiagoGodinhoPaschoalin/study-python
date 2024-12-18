import cv2, numpy

image_path: str = './../images_origin/'
image_name: str = '1a90'
image_extension: str = '.png'
img_read = '{}{}{}'.format(image_path, image_name, image_extension)
x: int = 2100
y: int = 2970
qrcode_data = 'dados do usuário e avaliação aqui...'

image: cv2.Mat = cv2.imread(img_read)
image = cv2.resize(image, (x, y))

# Definir a fonte e o tamanho do texto
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 0)  # Preto
font_thickness = 2

# Dividir o texto em linhas
text = "Aluno: Beltrano da Silva"

# Calcular a posição inicial do texto
y0, dy = 50, 30  # Posição inicial e espaçamento entre linhas

position = 0#Se montar um laço, aqui deve ser o indice do laço
text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
text_x = (image.shape[1] - text_size[0]) // 2
text_y = y0 + position * dy
cv2.putText(image, text, (150, 250), font, font_scale, font_color, font_thickness)
cv2.putText(image, text, (150, 300), font, font_scale, font_color, font_thickness)

# Mostrar a imagem
cv2.imshow('Image with Text', image)
cv2.waitKey(0)