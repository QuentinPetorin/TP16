from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QHBoxLayout,QVBoxLayout, QGridLayout, QTextEdit
import random

class CSI(QWidget):

    def __init__(self):

        QWidget.__init__(self)

        self.layout = QVBoxLayout()
        self.setMinimumSize(500,300)
        self.setWindowTitle("Cycle de l'ISEN de l'Ouest")
        self.label = QLabel("CSI")
        self.button = QPushButton("Changer le cycle")
        self.list = ["CSI","CIR","CENT","BIOST","EST","BIAST"]
        self.button.clicked.connect(self.buttonClicked)

        self.label.setText(random.choice(self.list))




        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def buttonClicked(self):

        print(random.choice(self.list))




if __name__ == "__main__":
    app = QApplication([])
    win = CSI()
    win.show()
    app.exec_()





