from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

from controller.dialog import Mydialog
from model.talaba import Talaba
from service.guruh_service import GuruhService
from service.talaba_service import TalabaService
from service.yunalish_service import YunalishService


class TalabaController(QWidget):
    ts = TalabaService()
    gs = GuruhService()
    ys = YunalishService()

    def __init__(self, win):
        self.win = win
        super(TalabaController, self).__init__()
        loadUi('view/student.ui', self)
        self.saqlashButton.clicked.connect(self.save)
        self.tozalashBtn.clicked.connect(self.tozalash)
        self.uchirishButton.clicked.connect(self.uchirish)
        self.uzgartirishButton.clicked.connect(self.uzgartirish)
        self.yunalishEdit.activated[str].connect(self.yunalishTanlash)
        self.yunalishToldir()
        self.oqish()
        self.table.cellClicked.connect(self.cell_was_clicked)
        self.tanlanganTalaba = False
        self.editRejim = False

    def yunalishTanlash(self, txt):
        id = txt.split("-", 1)[0]
        self.guruhToldir(id)

    def save(self):

        ism = self.ismEdit.toPlainText()
        familiya = self.familiyaEdit.toPlainText()
        sharif = self.sharifEdit.toPlainText()
        tugYil = self.dateEdit.text()
        guruh = str(self.guruhEdit.currentText())
        guruh = guruh.split("-", 1)[0]

        talaba = Talaba((0, ism, familiya, sharif, tugYil, guruh, ""))
        if self.ts.add(talaba):

            msg = QMessageBox()
            msg.setText("Qo'shildi")
            msg.time_to_wait = 4
            msg.setIcon(QMessageBox.Icon.Information)
            msg.exec_()
            self.tozalash()
        else:
            msg = QMessageBox()
            msg.setText("Xatolik bo'ldi")
            msg.time_to_wait = 4
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
        self.oqish()

        print(ism, familiya, sharif, tugYil, guruh)

    def tozalash(self):
        self.editRejim = False
        self.labelBosh.setText("Talaba qo'shish")

        self.ismEdit.setPlainText("")
        self.familiyaEdit.setPlainText("")
        self.sharifEdit.setPlainText("")
        # self.dateEdit.text()
        # self.guruhEdit.currentText()

    def guruhToldir(self, yunalish):
        guruhlar = None
        self.guruhEdit.clear()
        if yunalish:
            self.guruhEdit.setEnabled(True)
            guruhlar = self.gs.getByYunalish(yunalish)
            for guruh in guruhlar:
                self.guruhEdit.addItem(str(guruh.id) + '-' + guruh.nom)
        else:
            self.guruhEdit.setEnabled(False)
            self.guruhEdit.addItem("Yunalish tanlansin")

    def yunalishToldir(self):
        yunalishlar = self.ys.getAll()
        for yunalish in yunalishlar:
            self.yunalishEdit.addItem(str(yunalish.id) + '-' + yunalish.nom)
        self.yunalishTanlash(str(yunalishlar[0].id) + "-")

    def oqish(self):
        talabalar = self.ts.getAll()
        self.table.setRowCount(0)

        for i, talaba in enumerate(talabalar):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(talaba.id)))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(talaba.ism)))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(talaba.familiya)))
            self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(talaba.sharif)))
            self.table.setItem(i, 4, QtWidgets.QTableWidgetItem(str(talaba.tug_yil)))
            self.table.setItem(i, 5, QtWidgets.QTableWidgetItem(str(talaba.guruh)))
            self.table.setItem(i, 6, QtWidgets.QTableWidgetItem(str(talaba.yunalish)))

    def cell_was_clicked(self, row, column):
        print("Row %d and Column %d was clicked" % (row + 1, column + 1))
        id = self.table.item(row, 0).text()
        ism = self.table.item(row, 1).text()
        familiya = self.table.item(row, 2).text()
        sharif = self.table.item(row, 3).text()
        tugYil = self.table.item(row, 4).text()
        guruh = self.table.item(row, 5).text()
        yunalish = self.table.item(row, 6).text()

        self.tanlanganTalaba = Talaba((id, ism, familiya, sharif, tugYil, guruh, yunalish))
    def uchirish2(self,tgm):
        print('Ha')
        if self.ts.deleteById(self.tanlanganTalaba.id):
            self.tanlanganTalaba = False
            self.oqish()
        else:
            msg = Mydialog("O`chirishda xatolik")
            msg.xato()

    def uchirish(self):
        if self.editRejim:
            msg = Mydialog("Avval tahrirlashni bekor qiling !!!")
            msg.xato()
            return False
        if self.tanlanganTalaba:
            qm = QMessageBox()
            qm.setText("Siz rostdan ham "+self.tanlanganTalaba.ism+"ni o`chirmoqchimisiz ?")
            deleteButton = qm.addButton('O`chirish', qm.ActionRole)
            qm.setStandardButtons(QMessageBox.Cancel)
            deleteButton.clicked.connect(self.uchirish2)
            qm.exec_()
        else:
            msg = QMessageBox()
            msg.setText("Oldin jadvaldan talabani tanlang")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

    def uzgartirish(self):
        if self.tanlanganTalaba:
            self.editRejim = True
            self.labelBosh.setText("O'zgartirish")
            self.ismEdit.setPlainText(self.tanlanganTalaba.ism)
            self.familiyaEdit.setPlainText(self.tanlanganTalaba.familiya)
            self.sharifEdit.setPlainText(self.tanlanganTalaba.sharif)
            s = QDate.fromString(self.tanlanganTalaba.tug_yil,"yyyy-MM-dd")
            self.dateEdit.setDate(s)

        else:
            msg = QMessageBox()
            msg.setText("Avval talabani tanlang!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

