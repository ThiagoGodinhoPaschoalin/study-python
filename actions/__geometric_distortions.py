import cv2
import numpy as np
import random
from matplotlib import pyplot as plt
from datetime import datetime, timezone

class GeometricDistortions:
  def __init__(self, image_path: str = None):
    self.available_transformations = [
      'translate', 'rotate', 'scale', 'noise', 'brightness_contrast', 'directional_light', 'shadow'
    ]
    self.image_path = image_path

   # 1. Translação
  def __translate(self, img, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
  
  # 2. Rotação com ajuste de escala para manter a imagem visível
  def __rotate(self, img, angle):
    (h, w) = img.shape[:2]
    M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))
    M[0, 2] += (new_w / 2) - w // 2
    M[1, 2] += (new_h / 2) - h // 2
    return cv2.warpAffine(img, M, (new_w, new_h))
  
  # 3. Escala
  def __scale(self, img, fx, fy):
    return cv2.resize(img, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)

  # 4. Adicionar Ruído Gaussiano
  def __noise(self, img):
    mean = 0
    sigma = 10
    gaussian = np.random.normal(mean, sigma, img.shape).astype('uint8')
    noisy_image = cv2.add(img, gaussian)
    return noisy_image

  # 5. Brilho e Contraste
  def __brightness_contrast(self, img, alpha=1.0, beta=0):
    adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    return adjusted

  # 6. Iluminação Direcional
  def __directional_light(self, img, intensity=0.5, position=(0.5, 0.5)):
    h, w = img.shape[:2]
    mask = np.zeros((h, w), np.uint8)
    center_x, center_y = int(position[0] * w), int(position[1] * h)
    max_radius = max(center_x, center_y, w - center_x, h - center_y)
    for i in range(h):
        for j in range(w):
            distance = np.sqrt((center_x - j) ** 2 + (center_y - i) ** 2)
            mask[i, j] = max(0, 255 - int((distance / max_radius) * 255 * intensity))
    result = cv2.addWeighted(img, 1.0, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR), intensity, 0)
    return result

  # 7. Efeito de Sombra
  def __shadow(self, img, start=(0.5, 0), end=(1, 1), intensity=0.7):
    h, w = img.shape[:2]
    shadow_img = img.copy()
    shadow_mask = np.zeros((h, w), np.uint8)
    start_point = (int(start[0] * w), int(start[1] * h))
    end_point = (int(end[0] * w), int(end[1] * h))
    cv2.rectangle(shadow_mask, start_point, end_point, 255, -1)
    shadow_img = cv2.addWeighted(shadow_img, 1 - intensity, cv2.cvtColor(shadow_mask, cv2.COLOR_GRAY2BGR), intensity, 0)
    return shadow_img

  # Validar se tenho um caminho de imagem para manipulação
  def __get_image_path(self, image_path_ref: str = None) -> str:
    if image_path_ref is None and self.image_path is None:
      raise ValueError("É exigido uma imagem do tipo 'cv2.typing.MatLike' para manipulação.")
    
    if self.image_path is None:
      self.image_path = image_path_ref
    
    if image_path_ref is None:
      image_path_ref = self.image_path

    return image_path_ref

  #  Função para aplicar distorções geométricas em uma imagem
  def set_distortions(self,
    image_origin_path: str = None,
    selected_transformations: list[str] | str | None = [
      'translate', 'rotate', 'scale', 'noise', 'brightness_contrast', 'directional_light', 'shadow'],
    num_images=1) -> list[tuple[str, cv2.typing.MatLike]]:

    image_origin_path = self.__get_image_path(image_origin_path)

    image_origin = cv2.imread(image_origin_path)

    if selected_transformations == None or selected_transformations == "all":
      selected_transformations = self.available_transformations

    transformed_images: list[tuple[str, cv2.typing.MatLike]] = []

    for choice in selected_transformations:
      for _ in range(num_images):
        image = image_origin.copy()
        if choice == 'translate':
          tx, ty = random.randint(-35, 35), random.randint(-35, 35)
          transformed_img = self.__translate(image, tx, ty)
        elif choice == 'rotate':
          angle = random.uniform(-35, 35)
          transformed_img = self.__rotate(image, angle)
        elif choice == 'scale':
          fx, fy = random.uniform(0.4, 1.5), random.uniform(0.4, 1.5)
          transformed_img = self.__scale(image, fx, fy)
        elif choice == 'noise':
          transformed_img = self.__noise(image)
        elif choice == 'brightness_contrast':
          alpha = random.uniform(0.5, 1.5)
          beta = random.randint(-50, 50)
          transformed_img = self.__brightness_contrast(image, alpha=alpha, beta=beta)
        elif choice == 'directional_light':
          intensity = random.uniform(0.3, 0.7)
          position = (random.uniform(0, 1), random.uniform(0, 1))
          transformed_img = self.__directional_light(image, intensity=intensity, position=position)
        elif choice == 'shadow':
          start = (random.uniform(0, 0.5), random.uniform(0, 0.5))
          end = (random.uniform(0.5, 1), random.uniform(0.5, 1))
          intensity = random.uniform(0.3, 0.7)
          transformed_img = self.__shadow(image, start=start, end=end, intensity=intensity)
        
        transformed_images.append((choice, transformed_img))
    
    return transformed_images

  def show_plot_sample(self, image_path_2plot: str = None):

    image_path = self.__get_image_path(image_path_2plot)

    distorted_images = self.set_distortions(image_path)

    total = len(distorted_images) + 1

    # Apresentar amostra: imagem original e imagens transformadas
    plt.figure(figsize=(10, 10))
    plt.subplot(1, total, 1)
    plt.imshow(cv2.cvtColor(image_path, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis('off')
    for tuple in distorted_images:
      name, img = tuple
      plt.subplot(1, total, i + 2)
      plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
      plt.title(f"{name}")
      plt.axis('off')

    plt.show()

  def save_distortions(self, distorted_images: list[tuple[str, cv2.typing.MatLike]], folder_destination_path='./tmp'):

    if folder_destination_path.endswith("/"):
      folder_destination_path = folder_destination_path[:-1]
    
    for tuple in distorted_images:
      name, image = tuple
      datenow = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")
      filename = f"{folder_destination_path}/{name}_{datenow}.jpg"
      cv2.imwrite(filename, image)

