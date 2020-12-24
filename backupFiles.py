import os
import shutil

source = input("Enter source folder name: ")
destination = input("Enter destination name:")

source = source + "/"
destination = destination + "/"

listOfFiles = os.listdir(source)

for file in listOfFiles:
    shutil.move((source+file), destination)