import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Checkbox Örneği")

        central_widget = QWidget()
        layout = QVBoxLayout()

        checkbox = QCheckBox("Checkbox")
        checkbox.setChecked(False)  # Başlangıçta işaretli olması için

        checkbox.stateChanged.connect(self.durumGoster)  # Durum değiştiğinde fonksiyonu bağla

        layout.addWidget(checkbox)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def durumGoster(self, durum):
        print(durum)
        # if durum ==  Qt.CheckState.Checked:
        if durum ==  0: print("Checkbox işaretlendi")
        if durum ==  2: print("Checkbox işareti kaldırıldı")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

main()
