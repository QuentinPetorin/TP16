from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QHBoxLayout,QVBoxLayout, QGridLayout, QTextEdit, QProgressBar, QSlider

class text(QWidget):

    def __init__(self):

        QWidget.__init__(self)

        self.layout = QVBoxLayout()

        self.button = QPushButton("Changez mon texte")

        self.text = QTextEdit("affichage ici")

        self.layout.addWidget(self.button)

        self.layout.addWidget(self.text)

        self.setLayout(self.layout)
        self.counter = 1
        self.button.clicked.connect(self.modif)


# Fermeture de la fenetre
        #self.button.clicked.connect(self.close)

    #def close(self):
      #  QWidget.close(win)


    def modif(self):

         print("clic",self.counter)

         self.counter += 1





if __name__ == "__main__":
    app = QApplication([])
    win = text()
    win.show()
    app.exec_()







