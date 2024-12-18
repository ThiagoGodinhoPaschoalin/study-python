import cv2, numpy

# Definir dimensões da imagem
width, height = 600, 200
# Criar uma imagem em branco
image = numpy.ones((height, width, 3), dtype=numpy.uint8) * 255

# Definir a fonte e o tamanho do texto
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 0)  # Preto
font_thickness = 2

# Dividir o texto em linhas
text = "HELLO WORLD!"

# Calcular a posição inicial do texto
y0, dy = 50, 30  # Posição inicial e espaçamento entre linhas

position = 0#Se montar um laço, aqui deve ser o indice do laço
text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
text_x = (image.shape[1] - text_size[0]) // 2
text_y = y0 + position * dy
cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, font_thickness)

# Mostrar a imagem
cv2.imshow('Image with Text', image)
cv2.waitKey(0)