import os

from ImageFile import ImageFile

directory_path = "./Fotos_Prueba"

files = os.listdir(directory_path)
image_files = []
for file in files:
    path = f"{directory_path}/{file}"
    image_files.append(ImageFile(path))

cont = 0

for image_file in image_files:
    image_file.move_file()
    cont += 1
    print(int((cont / len(image_files)) * 100))
