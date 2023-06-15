import os
import string

dirName = "/home/fans/code/datasets/VOCwater_garbages/JPEGImages/"
li = os.listdir(dirName)
for filename in li:
    newname = filename
    newname = newname.split(".")
    if newname[-1] != "jpg":
        newname[-1] = "jpg"
        newname=str.join(".",newname)
        filename = dirName+filename
        newname = dirName+newname
        os.rename(filename,newname)
        print(newname,"updated successfully")
