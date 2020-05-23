from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QHBoxLayout,QVBoxLayout, QGridLayout, QTextEdit, QProgressBar, QSlider

class IHM(QWidget):

    def __init__(self):

        QWidget.__init__(self)

        self.layout = QHBoxLayout()
        self.setWindowTitle("IHM")


        self.bar = QProgressBar(self)
        self.slider = QSlider(self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(20)
        self.slider.valueChanged.connect(self.valuechange)


        self.layout.addWidget(self.bar)
        self.layout.addWidget(self.slider)
        self.setLayout(self.layout)




    def valuechange(self):
        size = self.slider.value()
        print(size)




if __name__ == "__main__":
    app = QApplication([])
    win = IHM()
    win.show()
    app.exec_()



