# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_pipe_new_project.ui',
# licensing of '_pipe_new_project.ui' applies.
#
# Created: Mon Jun 24 23:51:17 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ui_new_project_dialog(object):
    def setupUi(self, ui_new_project_dialog):
        ui_new_project_dialog.setObjectName("ui_new_project_dialog")
        ui_new_project_dialog.resize(347, 360)
        ui_new_project_dialog.setMinimumSize(QtCore.QSize(347, 360))
        ui_new_project_dialog.setMaximumSize(QtCore.QSize(347, 360))
        self.gridLayout = QtWidgets.QGridLayout(ui_new_project_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(ui_new_project_dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.le_projectPath_2 = QtWidgets.QLineEdit(self.frame_4)
        self.le_projectPath_2.setObjectName("le_projectPath_2")
        self.horizontalLayout_5.addWidget(self.le_projectPath_2)
        self.btn_folder_lookup_2 = QtWidgets.QToolButton(self.frame_4)
        self.btn_folder_lookup_2.setObjectName("btn_folder_lookup_2")
        self.horizontalLayout_5.addWidget(self.btn_folder_lookup_2)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.le_clientName_2 = QtWidgets.QLineEdit(self.frame_4)
        self.le_clientName_2.setObjectName("le_clientName_2")
        self.verticalLayout_3.addWidget(self.le_clientName_2)
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.le_projectName_2 = QtWidgets.QLineEdit(self.frame_4)
        self.le_projectName_2.setObjectName("le_projectName_2")
        self.verticalLayout_4.addWidget(self.le_projectName_2)
        self.formLayout_2.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.ui_resolution_x_2 = QtWidgets.QSpinBox(self.frame_4)
        self.ui_resolution_x_2.setMaximum(5000)
        self.ui_resolution_x_2.setProperty("value", 1920)
        self.ui_resolution_x_2.setObjectName("ui_resolution_x_2")
        self.horizontalLayout_6.addWidget(self.ui_resolution_x_2)
        self.ui_resolution_y_2 = QtWidgets.QSpinBox(self.frame_4)
        self.ui_resolution_y_2.setMaximum(9900)
        self.ui_resolution_y_2.setProperty("value", 1080)
        self.ui_resolution_y_2.setObjectName("ui_resolution_y_2")
        self.horizontalLayout_6.addWidget(self.ui_resolution_y_2)
        self.formLayout_2.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.le_fps_2 = QtWidgets.QLineEdit(self.frame_4)
        self.le_fps_2.setObjectName("le_fps_2")
        self.horizontalLayout_7.addWidget(self.le_fps_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.formLayout_2.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_2.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.ui_shotNumber_2 = QtWidgets.QSpinBox(self.frame_4)
        self.ui_shotNumber_2.setMaximum(1200)
        self.ui_shotNumber_2.setProperty("value", 1)
        self.ui_shotNumber_2.setObjectName("ui_shotNumber_2")
        self.horizontalLayout_8.addWidget(self.ui_shotNumber_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.formLayout_2.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.ui_complete_path_2 = QtWidgets.QLabel(self.frame_4)
        self.ui_complete_path_2.setObjectName("ui_complete_path_2")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.ui_complete_path_2)
        self.btn_OK = QtWidgets.QPushButton(self.frame_4)
        self.btn_OK.setObjectName("btn_OK")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.btn_OK)
        self.gridLayout_4.addWidget(self.frame_4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(ui_new_project_dialog)
        QtCore.QMetaObject.connectSlotsByName(ui_new_project_dialog)

    def retranslateUi(self, ui_new_project_dialog):
        ui_new_project_dialog.setWindowTitle(QtWidgets.QApplication.translate("ui_new_project_dialog", "Dialog", None, -1))
        self.le_projectPath_2.setPlaceholderText(QtWidgets.QApplication.translate("ui_new_project_dialog", "Project path...", None, -1))
        self.btn_folder_lookup_2.setText(QtWidgets.QApplication.translate("ui_new_project_dialog", "...", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("ui_new_project_dialog", "Mandatory fields", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("ui_new_project_dialog", "Client Name", None, -1))
        self.le_clientName_2.setPlaceholderText(QtWidgets.QApplication.translate("ui_new_project_dialog", "Client name..", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("ui_new_project_dialog", "Project Name", None, -1))
        self.le_projectName_2.setPlaceholderText(QtWidgets.QApplication.translate("ui_new_project_dialog", "Project name..", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("ui_new_project_dialog", "Resolution", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("ui_new_project_dialog", "FPS", None, -1))
        self.le_fps_2.setPlaceholderText(QtWidgets.QApplication.translate("ui_new_project_dialog", "25", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("ui_new_project_dialog", "Amount of shots", None, -1))
        self.ui_complete_path_2.setText(QtWidgets.QApplication.translate("ui_new_project_dialog", "Complete path", None, -1))
        self.btn_OK.setText(QtWidgets.QApplication.translate("ui_new_project_dialog", "OK", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui_new_project_dialog = QtWidgets.QDialog()
    ui = Ui_ui_new_project_dialog()
    ui.setupUi(ui_new_project_dialog)
    ui_new_project_dialog.show()
    sys.exit(app.exec_())
