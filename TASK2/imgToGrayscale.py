from PIL import Image
import numpy as np

image = Image.open('road.jpg')
width, height = image.size

grayscaleArray = np.zeros((height, width, 3))
for i in range(width - 1, 0, -1):
    for j in range(0, height - 1, 1):
        r, g, b = image.getpixel((i, j))
        grayscale = (r + g + b) / 3
        for k in range(3):
            grayscaleArray[j][i][k] = grayscale
            k += 1

grayscaleImage = Image.fromarray(grayscaleArray.astype(np.uint8))
grayscaleImage.save("grayscaleRoad.jpg")