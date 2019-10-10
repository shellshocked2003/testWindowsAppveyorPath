import sys
import os

counter = 0
filePath = "./"

for i in range(0,100):
    filePath = filePath + "mirrorInTheBathroom" + str(i) + "/"

if not os.path.exists(filePath):
    os.makedirs(filePath)
    
with open(filePath + "PleaseTalkFree.txt", 'w') as longFile:
    longFile.write("Wow, this is a really deep directory structure...\n")
