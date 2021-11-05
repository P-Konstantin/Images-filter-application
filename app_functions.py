import cv2
import numpy as np
import os


def filter(filestr):
    """Преобразует изображение в скетч."""

    # Преобразуем файл в массив numpy
    npimg = np.fromstring(filestr, np.uint8)

    # Преобразуем полученный массив numpy в
    # данные формата изображения, с загрузкой цвета изображения
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Делаем изображение серым
    grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Делаем инверсию элементов входного массива
    invert = cv2.bitwise_not(grey_image)

    # Сглаживаем изображение, удаляем посторонние пиксели,
    # которые являются шумом на изображении
    blur = cv2.GaussianBlur(invert, (21, 21), 0)

    # Делаем инверсию
    inverted_blue = cv2.bitwise_not(blur)

    # Выполняем поэлементное деление массива на массив,
    # получаем конечное изображение
    sketch = cv2.divide(grey_image, inverted_blue, scale=256.0)

    # Сохраняем в переменную путь до файла
    path = "static/sketch/"

    # Сохраняем изображение в указанной директории,
    # в указанном формате
    result = cv2.imwrite(os.path.join(path,"sketch.png"), sketch)

    return result








