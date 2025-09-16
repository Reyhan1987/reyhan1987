from PyQt6.QtWidgets import *
aa=QApplication([])
bb=QWidget()
icerik=QVBoxLayout()
icerik.addWidget(QPushButton("Tıkla"))
icerik.addWidget(QPushButton("Dene"))
icerik.addWidget(QLabel("Bilgi"))
bb.setLayout(icerik)
bb.show()
aa.exec()

