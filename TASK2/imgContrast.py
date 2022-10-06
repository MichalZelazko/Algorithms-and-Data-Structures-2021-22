from PIL import Image
import numpy as np

image = Image.open('yoda.jpeg')
image = image.convert(mode='L')
imgArray = np.asarray(image)
imgFlattened = imgArray.flatten()

width, height = image.size

histogram = np.bincount(imgFlattened, minlength=256)

probabilityHistogram = np.zeros(256)

for k in range(256):
    probabilityHistogram[k] = histogram[k] / (width * height)

cumulativeArray = np.cumsum(probabilityHistogram)
transformMap = np.floor(255 * cumulativeArray).astype(np.uint8)
imgList = list(imgArray.flatten())
equalizedImgList = [transformMap[pixel] for pixel in imgList]
equalizedImgArray = np.reshape(np.asarray(equalizedImgList), imgArray.shape)
equalizedImg = Image.fromarray(equalizedImgArray)
equalizedImg.save("contrastYoda.jpeg")