import os

from PIL import Image

directory_path = "./Fotos_Prueba"
dates = []
month_names = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
               "Noviembre", "Diciembre"]

files = os.listdir(directory_path)
correct_files = []
incorrect_files = []


def check_files(files):
    for file in files:
        path = f"{directory_path}/{file}"
        try:
            Image.open(path)._getexif()[36867]
            correct_files.append(file)
        except TypeError:
            incorrect_files.append(file)


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
        year = date[:4]
        years.append(year)

    return years


def get_months(dates):
    months = []
    for date in dates:
        month = date[5:7]
        months.append(month)

    return months


def create_years_directories(years):
    for year in years:
        try:
            os.mkdir(f"Fotos_Ordenadas/{year}")
        except FileExistsError:
            pass


def create_months_directories(years, months):
    for year in years:
        for month in months:
            try:
                os.mkdir(f"Fotos_Ordenadas/{year}/{month} {month_names[int(month) - 1]}")
            except FileExistsError:
                pass


check_files(files)

for file in correct_files:
    dates.append(get_date_taken(directory_path, file))

print(correct_files)
print(incorrect_files)
print(dates)

create_main_directory()
create_years_directories(get_years(dates))
create_months_directories(get_years(dates), get_months(dates))
