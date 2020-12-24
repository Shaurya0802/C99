import os
import shutil

path = "E:/Python/C99/folder"
print("Before Copying File: ")
print(os.listdir(path))

source = "E:/Python/C99/abc"
destination = "E:/Python/C99-test"
dest = shutil.move(source, destination)
print("After Copying file:")
print(os.listdir(path))