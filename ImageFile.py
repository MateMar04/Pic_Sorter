import os
import shutil

from PIL import Image


class ImageFile:
    def __init__(self, image_path):
        self.image_path = image_path
        self.month_names = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
                            "Octubre",
                            "Noviembre", "Diciembre"]

    def get_date_taken(self):
        try:
            return Image.open(self.image_path)._getexif()[36867]
        except TypeError:
            return "9999:12:31 23:59:59"

    def get_year_taken(self):
        return self.get_date_taken()[:4]

    def get_month_taken(self):
        return self.get_date_taken()[5:7]

    def get_dst_dir(self):
        return f"Fotos_Ordenadas/{self.get_year_taken()}/{self.get_month_taken()}_{self.month_names[int(self.get_month_taken()) - 1]}"

    def create_dir(self):
        try:
            dir = f"Fotos_Ordenadas"
            if not os.path.isdir(dir):
                os.mkdir(dir)
            dir += f"/{self.get_year_taken()}"
            if not os.path.isdir(dir):
                os.mkdir(dir)
            dir += f"/{self.get_month_taken()}_{self.month_names[int(self.get_month_taken()) - 1]}"
            if not os.path.isdir(dir):
                os.mkdir(dir)
        except FileExistsError:
            pass

    def move_file(self, dst_dir):
        shutil.copy2(self.image_path, dst_dir)
