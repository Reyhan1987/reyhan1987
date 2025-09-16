from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class Pencere(QMainWindow):
    def __init__(self):
        super(Pencere, self).__init__()

        self.setWindowTitle("... Uygulaması")
        self.setFixedWidth(500)
        self.setFixedHeight(300)

        layout = QVBoxLayout() # layout = QHBoxLayout()

        pixmap = QPixmap('indir.jpg') # .py dosyasının olduğu yerde
        label2 = QLabel(self)
        label2.setGeometry(100,50,200,100)
        label2.setPixmap(pixmap)
        layout.addWidget(QLabel("Kullanıcı adı:"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Şifre:"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QCheckBox("Beni hatırla"))
        layout.addWidget(QPushButton("Giriş yap"))
        layout.addWidget(QLabel("..."))

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

uygulama = QApplication([])
anapencere = Pencere()
anapencere.show()
uygulama.exec()