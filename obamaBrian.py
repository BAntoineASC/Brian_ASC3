from Myro import *
from Graphics import *

obamaDarkBlue = makeColor(0,51,76)
obamaRed = makeColor(217, 26, 33)
obamaBlue = makeColor(112,150,158)
obamaYellow = makeColor(252, 227, 166)
pic = makePicture(pickAFile())
#obama(pic)

for pixel in getPixels(pic):
      gray = getGray(pixel)
      
      if gray > 182:
             setColor(pixel, obamaYellow)
      #red = getRed(pixel)
      elif gray >120:
             setColor(pixel, obamaDarkBlue)
      #black = getGreen(pixel)
      elif gray > 62:
             setColor(pixel, obamaRed)
      #yellow = getBlue(pixel)
      elif gray > 200:
             setColor(pixel, obamaBlue)
show(pic)    