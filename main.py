# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton

from ui_calculatrice import Ui_MainWindow
from Calculator import Calculator

class MainWindow(QMainWindow):
    def __init__(self,x=0,y=0, w=411,h=489):
         super(MainWindow, self).__init__()
         self.calc = Calculator()
         self.initUi()
         for i in range(0, 10):
             getattr(self.ui, "num_" + str(i)).clicked.connect(self.addNumber)
         self.setWindowTitle("Calculatrice à Julien")

    #.clearHistory(backward()) pour effacer par en arriere

    def initUi(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def addNumber(self):
        butt = self.sender()
        old = self.ui.Montrer.toPlainText()
        newText = old + butt.text()
        self.ui.Montrer.setText(newText)
        #self.ui.Montrer.setText(butt.text())
        print(butt.text())


def window():
    app = QApplication(sys.argv)
    win = MainWindow()

    app.setActiveWindow(win)
    win.show()

    sys.exit(app.exec())

if __name__ == "__main__":
     window()
