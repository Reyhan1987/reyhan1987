import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit,QPushButton,QLabel

class Pencere(QWidget):
    def __init__(self):
        super().__init__
        self.ozellikekle()
        self.ekozellikekle()
        self.button.clicked.connect(self.tiklandi)

    def ozellikekle(self):
        self.resize(300,300)
        self.move(500,100)
        self.setWindowTitle("Basit Pencere")
    
    def ekozellikekle(self):
        self.input=QLineEdit("Birşey yaz", self)
        self.input.setGeometry(10,10,200,25)
        self.buton=QPushButton("Ekrana yaz",self)
        self.buton.setGeometry(10,50,200,75)
        self.label=QLabel("Sonuc",self)
        self.label.setGeometry(10,110,200,75)
    
    def tiklandi(self):
        self.label.setText(self.input.text())

app=QApplication(sys.argv)
pencere=Pencere()
pencere.show()
sys.exit(app.exec_())