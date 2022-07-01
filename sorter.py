import os
import shutil

from ImageFile import ImageFile

directory_path = "./Fotos_Prueba"
dates = []
month_names = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
               "Noviembre", "Diciembre"]

files = os.listdir(directory_path)
image_files = []
for file in files:
    path = f"{directory_path}/{file}"
    image_files.append(ImageFile(path))

for image_file in image_files:
    image_file.create_dir()
    image_file.move_file(image_file.get_dst_dir())
