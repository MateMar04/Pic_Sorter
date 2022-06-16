import os

from PIL import Image

directory_path = "./Fotos_Prueba"


def get_files(directory):
    return os.listdir(directory)


def get_number_of_files(files):
    return len(files)


def get_date_taken(directory, file):
    path = f"{directory}/{file}"
    try:
        return Image.open(path)._getexif()[36867]
    except TypeError:
        pass


for i in get_files(directory_path):
    print(get_date_taken(directory_path, i))
