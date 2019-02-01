# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

CURRENT_SELECTION = None


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(648, 566)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.theme_list = QtWidgets.QListWidget(self.centralWidget)
        self.theme_list.setGeometry(QtCore.QRect(10, 460, 491, 91))
        self.theme_list.setObjectName("theme_list")
        self.theme_view = QtWidgets.QLabel(self.centralWidget)
        self.theme_view.setGeometry(QtCore.QRect(10, 10, 631, 431))
        self.theme_view.setObjectName("theme_view")
        self.load_button = QtWidgets.QPushButton(self.centralWidget)
        self.load_button.setGeometry(QtCore.QRect(510, 460, 131, 31))
        self.load_button.setObjectName("load_button")
        self.package_button = QtWidgets.QPushButton(self.centralWidget)
        self.package_button.setGeometry(QtCore.QRect(510, 490, 131, 31))
        self.package_button.setObjectName("package_button")
        self.revert_button = QtWidgets.QPushButton(self.centralWidget)
        self.revert_button.setGeometry(QtCore.QRect(510, 520, 131, 31))
        self.revert_button.setObjectName("revert_button")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.theme_list.itemClicked.connect(self.onclick_theme_list)
        self.load_button.clicked.connect(self.onclick_load_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.load_button.setText(_translate("MainWindow", "&Load"))
        self.package_button.setText(_translate("MainWindow", "&Package"))
        self.revert_button.setText(_translate("MainWindow", "&Revert"))



        # Quick and dirty...
        USER = os.environ.get("USER")
        I3P_DIR = "/home/" + USER + "/.config/i3packager/"


        if not (os.path.isdir(I3P_DIR) and os.path.isfile(I3P_DIR + "config")):
            print("[-] Please run CLI application first to generate config file and directory")
            quit()

        theme_dir_listing = os.listdir(I3P_DIR)
        for dir in theme_dir_listing:
            if os.path.isdir(I3P_DIR + dir) and dir != ".last":
                self.theme_list.addItem(dir)


    def onclick_load_button(self):
        if CURRENT_SELECTION is None or CURRENT_SELECTION == "":
            fail_box = QtWidgets.QMessageBox()
            fail_box.setText("Please select a theme to load!")
            fail_box.exec_()





    def onclick_theme_list(self):
        global CURRENT_SELECTION
        selected_item = self.theme_list.selectedItems()[0]
        CURRENT_SELECTION = selected_item.text()


        # Quick and dirty...
        USER = os.environ.get("USER")
        I3P_DIR = "/home/" + USER + "/.config/i3packager/"
        image = QtGui.QImage(I3P_DIR + selected_item.text() + '/' + selected_item.text() + '.png')
        image = QtGui.QPixmap.fromImage(image)
        self.theme_view.setPixmap(image.scaled(self.theme_view.width(),self.theme_view.height()))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

