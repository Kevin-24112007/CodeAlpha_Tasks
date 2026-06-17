import os
import shutil

print("Move all .jpg files from a folder to a new folder\n")

source = input("Enter the source folder path: ")
if not os.path.exists(source):
    print("Source folder is not found")
    exit()

destination  = os.path.join(source, "JPG_FILES")
if not os.path.exists(destination):
    os.mkdir(destination)

for file in os.listdir(source):
    if file.endswith(".jpg"):
        shutil.move(os.path.join(source, file), os.path.join(destination,file))
        print(f"{file} has been moved to {destination}")

print("\nAll JPG Files were moved into a new folder")