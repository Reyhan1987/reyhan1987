import sys
from PyQt6 import QtWidgets
app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Merhaba")
button.setFixedSize(100, 100)
button.show()
app.exec()