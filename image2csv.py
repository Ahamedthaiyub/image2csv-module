from PIL import Image
import numpy as np
import os, os.path, time 

format='.jpg'
myDir = "Lotus1" 
def createFileList(myDir, format='.jpg'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
            for name in files:
               if name.endswith(format):
                  fullName = os.path.join(root, name)
                  fileList.append(fullName)
                  return fileList

fileList = createFileList(myDir)
fileFormat='.jpg'
for fileFormat in fileList:
 format = '.jpg'
 # get original image parameters...
 width, height = fileList.size
 format = fileList.format
 mode = fileList.mode
 # Make image Greyscale
 img_grey = fileList.convert('L')
 # Save Greyscale values
 value = np.asarray(fileList.getdata(),dtype=np.float64).reshape((fileList.size[1],fileList.size[0]))
 np.savetxt("img_pixels.csv", value, delimiter=',')
