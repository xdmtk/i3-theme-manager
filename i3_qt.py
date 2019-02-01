# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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

