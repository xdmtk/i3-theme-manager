from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1003, 452)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.theme_list = QtWidgets.QListWidget(self.centralWidget)
        self.theme_list.setGeometry(QtCore.QRect(10, 10, 631, 431))
        self.theme_list.setObjectName("theme_list")
        self.theme_view = QtWidgets.QGraphicsView(self.centralWidget)
        self.theme_view.setGeometry(QtCore.QRect(650, 10, 341, 291))
        self.theme_view.setObjectName("theme_view")
        self.load_button = QtWidgets.QPushButton(self.centralWidget)
        self.load_button.setGeometry(QtCore.QRect(650, 310, 161, 61))
        self.load_button.setObjectName("load_button")
        self.package_button = QtWidgets.QPushButton(self.centralWidget)
        self.package_button.setGeometry(QtCore.QRect(830, 310, 161, 61))
        self.package_button.setObjectName("package_button")
        self.revert_button = QtWidgets.QPushButton(self.centralWidget)
        self.revert_button.setGeometry(QtCore.QRect(650, 380, 341, 61))
        self.revert_button.setObjectName("revert_button")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Event handlers
        self.theme_list.itemClicked.connect(self.onclick_theme_list)



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



    def onclick_theme_list(self):

        selected_item = self.theme_list.selectedItems()

        # Quick and dirty...
        USER = os.environ.get("USER")
        I3P_DIR = "/home/" + USER + "/.config/i3packager/"












    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.load_button.setText(_translate("MainWindow", "&Load"))
        self.package_button.setText(_translate("MainWindow", "&Package"))
        self.revert_button.setText(_translate("MainWindow", "&Revert"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


