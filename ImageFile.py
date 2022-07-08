import os
import shutil

from PIL import Image
from PIL import UnidentifiedImageError


class ImageFile:
    def __init__(self, image_path):
        self.image_path = image_path
        self.month_names = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
                            "Octubre", "Noviembre", "Diciembre"]

    def get_date_taken(self):
        try:
            return Image.open(self.image_path)._getexif()[36867]
        except TypeError:  # IMAGENES SIN EXIF
            return self.generate_name(os.path.basename(self.image_path))
        except UnidentifiedImageError:  # SON VIDEOS
            return "9998:12:31 23:59:59"
        except KeyError:  # NO SON IMAGENES
            return "9999:12:31 23:59:59"

    def get_year_taken(self):
        return self.get_date_taken()[:4]

    def get_month_taken(self):
        return self.get_date_taken()[5:7]

    def create_dir(self):
        try:
            dir = f"Fotos_Ordenadas"
            if not os.path.isdir(dir):
                os.mkdir(dir)
            dir += f"/{self.get_year_taken()}"
            if not os.path.isdir(dir):
                os.mkdir(dir)
            dir += f"/{self.get_month_taken()}_{self.month_names[int(self.get_month_taken())]}"
            if not os.path.isdir(dir):
                os.mkdir(dir)
            return dir
        except FileExistsError:
            pass

    def move_file(self):
        dst_dir = self.create_dir()
        shutil.copy2(self.image_path, dst_dir)

    def generate_name(self, file_name):
        if file_name.endswith(".jpg") or file_name.endswith(".webp") or file_name.endswith(".jpeg"):
            if file_name.startswith("IMG-"):
                year = file_name[4:8]
                month = file_name[8:10]
                return f"{year}:{month}:01 00:00:00"
            else:
                return "9997:12:31 23:59:59"
        else:
            return "9997:12:31 23:59:59"
