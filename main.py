import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.uic import loadUi

# from qt_material import apply_stylesheet
from controller import LoginController, DashboardController, TalabaController, GuruhController, YunalishController


class Main(QMainWindow):
    def __init__(self):

        self.app = QApplication(sys.argv)
        # apply_stylesheet(self.app, theme="light_teal.xml")
        super(Main, self).__init__()
        loadUi('view/main.ui', self)

        #Menu
        dash = QAction("Bosh sahifa")
        dash.triggered.connect(self.dashboardAction)
        self.menuBar().addAction(dash)
        st = QAction("Talabalar")
        st.triggered.connect(self.studentAction)
        self.menuBar().addAction(st)
        gur = QAction("Guruhlar ")
        gur.triggered.connect(self.guruhAction)
        self.menuBar().addAction(gur)
        y = QAction("Yo'nalishlar")
        y.triggered.connect(self.yunalishAction)
        self.menuBar().addAction(y)

        self.widget = QtWidgets.QStackedWidget()
        self.widget.setGeometry(0, 20, 6000, 4000)
        #ekranga o`lcham berish:
        self.setMaximumSize(1000,500)
        self.setMinimumSize(800,400)
        self.layout().addWidget(self.widget)

        self.widget.geometry().center()
        self.login = LoginController(self)

        self.currentWidget = None

        self.loadWindows()
        #login parol qismi
        self.login.show()
        self.app.exec_()

    def studentAction(self):
        self.showWidget(self.talaba)

    def guruhAction(self):
        self.showWidget(self.guruh)

    def yunalishAction(self):
        self.showWidget(self.yunalish)

    def dashboardAction(self):
        self.showWidget(self.dashboard)

    def showWidget(self, w):
        self.widget.removeWidget(self.currentWidget)
        self.widget.addWidget(w)
        self.currentWidget = w

    def loadWindows(self):
        self.dashboard = DashboardController(self)
        self.talaba = TalabaController(self)
        self.guruh = GuruhController(self)
        self.yunalish = YunalishController(self)
        self.showWidget(self.dashboard)


Main()
