import sys
from PyQt6.QtWidgets import *
uyg = QApplication([])
pencere = QWidget()
pencere.show()  
uyg.exec()
app = QApplication(sys.argv)
window = QMainWindow()
window.show()
app.exec()
