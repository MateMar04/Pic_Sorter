import sys
import os
from PIL import Image

path = "C:/Users/mateo/Desktop/Fotos_Prueba"

number_files = os.listdir(path)
files_list = []


def get_files_list():
    for file in number_files:
        files_list.append(file)
    return files_list


def get_date_taken(path):
    print(Image.open(path)._getexif()[36867])   
    return Image.open(path)._getexif()[36867]


"""
def get_file_date():
    for file in files_list:
        file_path = "C:/Users/mateo/Desktop/Fotos_Prueba/" + file
        date = os.path.(file_path)
        print(date)
    return date
"""

get_files_list()
get_date_taken(path)
