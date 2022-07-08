import os
import sys
from tkinter import *
from tkinter import filedialog

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QApplication

from ImageFile import ImageFile
from SorterWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @Slot()
    def src_dir_slot(self):
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        print(folder_selected)
        self.ui.lb_src_dir.setText(folder_selected)
        return folder_selected

    @Slot()
    def dst_dir_slot(self):
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        print(folder_selected)
        self.ui.lb_dst_dir.setText(folder_selected)
        return folder_selected

    @Slot()
    def go_slot(self):
        print("go_slot")

    @Slot()
    def progress_changed_slot(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

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
