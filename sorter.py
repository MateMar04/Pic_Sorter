import os

from PIL import Image

directory_path = "./Fotos_Prueba"
dates = []


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


def create_main_directory():
    try:
        os.mkdir("Fotos_Ordenadas")
    except FileExistsError:
        pass


def get_years(dates):
    years = []
    for date in dates:
        try:
            year = date[:4]
        except TypeError:
            year = "NONE"

        years.append(year)

    return years


def create_years_directories(years):
    for year in years:
        try:
            os.mkdir(f"Fotos_Ordenadas/{year}")
        except FileExistsError:
            pass


for i in get_files(directory_path):
    dates.append(get_date_taken(directory_path, i))

create_main_directory()
create_years_directories(get_years(dates))
