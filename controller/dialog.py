from PyQt5.QtWidgets import QMessageBox


class Mydialog(QMessageBox):
    def __init__(self, text):
        super(Mydialog, self).__init__()
        self.setText(text)
    def oddiy(self):
        self.setIcon(self.Information)
        self.exec_()
    def xato(self):
        self.setIcon(self.Critical)
        self.exec_()
