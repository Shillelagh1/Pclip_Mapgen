from PIL import Image
import numpy


def numberToHex(x):
    hexStr = hex(x)[2:]
    return ((3 - len(hexStr)) * "0") + hexStr


regionCharacters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
regionColors = []
wMap_Image = Image.open("wmap.bmp")
wMap_Array = numpy.array(wMap_Image)
print(len(wMap_Array))
print(len(wMap_Array[0]))
text = numberToHex(len(wMap_Array)) + numberToHex(len(wMap_Array[0]))
print(text)
for xArray in wMap_Array:
    for pixel in xArray:
        pixelColor = (pixel[0], pixel[1], pixel[2])
        if sum(pixelColor) == 0:
            text += "X"
        else:
            if pixelColor in regionColors:
                text += regionCharacters[regionColors.index(pixelColor)]
            else:
                regionColors.append(pixelColor)

file = open("map_txt.txt", "w")
file.write(text)
