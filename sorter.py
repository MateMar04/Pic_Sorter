import os

from PIL import Image

directory_path = "./Fotos_Prueba"
dates = []
months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
          "Noviembre", "Diciembre"]


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


def create_months_directories(years):
    for year in years:
        for month in range(1, 13):
            try:
                os.mkdir(f"Fotos_Ordenadas/{year}/{month} {months[month - 1]}")
            except FileExistsError:
                pass


for i in get_files(directory_path):
    dates.append(get_date_taken(directory_path, i))

create_main_directory()
create_years_directories(get_years(dates))
create_months_directories(get_years(dates))
