from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class Calcul(QWidget):

    def __init__(self,liste=[]):

        QWidget.__init__(self)
        self.liste = liste

        self.layout = QGridLayout()
        self.text = QLineEdit()
        self.buttonC = QPushButton('C')
        self.buttonCE = QPushButton('CE')
        self.button7 = QPushButton('7')
        self.button8 = QPushButton('8')
        self.button9 = QPushButton('9')
        self.buttonDiv = QPushButton('/')
        self.button4 = QPushButton('4')
        self.button5 = QPushButton('5')
        self.button6 = QPushButton('6')
        self.buttonMult = QPushButton('*')
        self.button1 = QPushButton('1')
        self.button2 = QPushButton('2')
        self.button3 = QPushButton('3')
        self.buttonSoust = QPushButton('-')
        self.button0 = QPushButton('0')
        self.buttonVirgule = QPushButton('.')
        self.buttonEgale = QPushButton('=')
        self.buttonAdd = QPushButton('+')



        self.layout.addWidget(self.text,0,0,1,4,Qt.Alignment())
        self.layout.addWidget(self.buttonC,1,0,1,2,Qt.Alignment())
        self.layout.addWidget(self.buttonCE, 1, 2,1,2, Qt.Alignment())
        self.layout.addWidget(self.button7, 2, 0, Qt.Alignment())
        self.layout.addWidget(self.button8, 2, 1, Qt.Alignment())
        self.layout.addWidget(self.button9, 2, 2, Qt.Alignment())
        self.layout.addWidget(self.buttonDiv, 2, 3, Qt.Alignment())
        self.layout.addWidget(self.button4, 3, 0, Qt.Alignment())
        self.layout.addWidget(self.button5, 3, 1, Qt.Alignment())
        self.layout.addWidget(self.button6, 3, 2, Qt.Alignment())
        self.layout.addWidget(self.buttonMult, 3, 3, Qt.Alignment())
        self.layout.addWidget(self.button1, 4, 0, Qt.Alignment())
        self.layout.addWidget(self.button2, 4, 1, Qt.Alignment())
        self.layout.addWidget(self.button3, 4, 2, Qt.Alignment())
        self.layout.addWidget(self.buttonSoust, 4, 3, Qt.Alignment())
        self.layout.addWidget(self.button0, 5, 0, Qt.Alignment())
        self.layout.addWidget(self.buttonVirgule, 5, 1, Qt.Alignment())
        self.layout.addWidget(self.buttonEgale, 5, 2, Qt.Alignment())
        self.layout.addWidget(self.buttonAdd, 5, 3, Qt.Alignment())





        self.setLayout(self.layout)
        self.buttonC.clicked.connect(self.affC)
        self.buttonCE.clicked.connect(self.affCE)
        self.button7.clicked.connect(self.aff7)
        self.button8.clicked.connect(self.aff8)
        self.button9.clicked.connect(self.aff9)
        self.buttonDiv.clicked.connect(self.affDiv)
        self.button4.clicked.connect(self.aff4)
        self.button5.clicked.connect(self.aff5)
        self.button6.clicked.connect(self.aff6)
        self.buttonMult.clicked.connect(self.affMult)
        self.button1.clicked.connect(self.aff1)
        self.button2.clicked.connect(self.aff2)
        self.button3.clicked.connect(self.aff3)
        self.buttonSoust.clicked.connect(self.affSous)
        self.button0.clicked.connect(self.aff0)
        self.buttonVirgule.clicked.connect(self.affVirgule)
        self.buttonEgale.clicked.connect(self.affEgale)
        self.buttonAdd.clicked.connect(self.affAdd)
        self.list =[]


    def affC(self):
        newnumber = str(0)
        self.liste.append(7)
        self.text.setText(newnumber)

    def affCE(self):
        self.liste.append(7)
        newnumber = str(0)
        self.text.setText(newnumber)

    def aff7(self):

        newnumber = str(7)
        self.liste.append(7)
        self.text.setText(newnumber)


    def aff8(self):
        newnumber = str(8)
        self.text.setText(newnumber)
        self.liste.append(8)

    def aff9(self):
        newnumber = str(9)
        self.text.setText(newnumber)
        self.liste.append(9)

    def affDiv(self):
        newnumber = str('/')
        self.text.setText(newnumber)
        self.liste.append('/')

    def aff4(self):
        newnumber = str(4)
        self.text.setText(newnumber)
        self.liste.append(4)

    def aff5(self):
        newnumber = str(5)
        self.text.setText(newnumber)
        self.liste.append(5)

    def aff6(self):
        newnumber = str(6)
        self.text.setText(newnumber)
        self.liste.append(6)

    def affMult(self):
        newnumber = str('*')
        self.text.setText(newnumber)
        self.liste.append('*')

    def aff1(self):
        newnumber = str(1)
        self.text.setText(newnumber)
        self.liste.append(1)

    def aff2(self):
        newnumber = str(2)
        self.text.setText(newnumber)
        self.liste.append(2)

    def aff3(self):
        newnumber = str(3)
        self.text.setText(newnumber)
        self.liste.append(3)

    def affSous(self):
        newnumber = str('-')
        self.text.setText(newnumber)
        self.liste.append('-')

    def aff0(self):
        newnumber = str(0)
        self.text.setText(newnumber)
        self.liste.append(0)

    def affVirgule(self):
        newnumber = str('.')
        self.text.setText(newnumber)
        self.liste.append('.')

    def affEgale(self):
        newnumber = str('=')
        self.text.setText(newnumber)
        self.liste.append('=')

    def affAdd(self):
        newnumber = str('+')
        self.text.setText(newnumber)
        self.liste.append('+')














if __name__ == "__main__":
    app = QApplication([])
    win = Calcul()
    win.show()
    app.exec_()


