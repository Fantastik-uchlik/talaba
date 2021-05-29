import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QLabel, QMessageBox
from PyQt5.uic import loadUi

from service.profil_service import ProfilService


class LoginController(QMainWindow):
    profService = ProfilService()

    def __init__(self, main):
        self.main = main
        super(LoginController,self).__init__()
        loadUi('view/login.ui', self)
        self.kirishButton.clicked.connect(self.kirishFunc)
        self.chiqishButton.clicked.connect(self.chiqishFunc)

    def kirishFunc(self):
        login = self.login.text()
        parol = self.parol.text()

        a = self.profService.getByLoginAndPassword(login, parol)

        if a:
            print(a.ism)

            self.main.show()
            self.close()

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Talaba")
            msg.setText("Login yoki parol noto'g'ri")

            msg.setIcon(QMessageBox.Critical)

            # my_dialog.layout().addItem(label)
            x = msg.exec_()

    def chiqishFunc(self):
        self.main.app.exit()