import os
import shutil

path = input("enter the path:")
files = os.listdir(path)

for file in files:
    filename,extention = os.path.splitext(file)
    extension =extention[1:]

    if os.path.exists(path+ '/' +extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
