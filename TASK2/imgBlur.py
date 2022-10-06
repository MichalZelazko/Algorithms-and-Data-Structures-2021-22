from PIL import Image
import numpy as np

image = Image.open('road.jpg')
image = image.convert(mode='L')

width, height = image.size

grayscaleArray = np.asarray(image)
blurredArray = grayscaleArray.copy()

squareMaskSize = 71

summedAreaTable = np.full((height, width), 0)
summedAreaTableDivider = squareMaskSize**2

for row in range(height):
    for col in range(width):
        if col > 0:
            summedAreaTable[row][col] = grayscaleArray[row][col] + summedAreaTable[row][col - 1]
            if row > 0:
                summedAreaTable[row][col] += summedAreaTable[row - 1][col] - summedAreaTable[row - 1][col - 1]
        else:
            summedAreaTable[row][col] = grayscaleArray[row][col]
            if row > 0:
                summedAreaTable[row][col] += summedAreaTable[row - 1][col]
    

for row in range(height - squareMaskSize):
    for col in range(width - squareMaskSize):
        meanFilter = (summedAreaTable[row + squareMaskSize][col + squareMaskSize] - summedAreaTable[row + squareMaskSize][col] - summedAreaTable[row][col + squareMaskSize] + summedAreaTable[row][col]) / summedAreaTableDivider
        blurredArray[row, col] = meanFilter
blurredImage = Image.fromarray(blurredArray.astype(np.uint8))
blurredImage.save("blurredRoad.jpg")