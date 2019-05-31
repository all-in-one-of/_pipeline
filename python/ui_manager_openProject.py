from ui.Project_manager_OpenProject import Ui_OpenProject
from PySide2 import QtWidgets
from general_functions import go_folder
import os

temp_path = r'C:\Users\Hernan\Documents\HERNAN\_projects'
go_folder(temp_path)


class UiCreation(Ui_OpenProject, QtWidgets.QMainWindow):
    def __init__(self):
        super(UiCreation, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = UiCreation()

    qt_app.show()
    app.exec_()
