import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ComboBox Örneği")

        central_widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Bir öğe seçin:")
        layout.addWidget(label)

        combobox = QComboBox()
        combobox.addItem("Seçenek 1")
        combobox.addItem("Seçenek 2")
        combobox.addItem("Seçenek 3")
        combobox.currentIndexChanged.connect(self.secileniGoster)  # Seçim değiştiğinde fonksiyonu bağla

        layout.addWidget(combobox)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def secileniGoster(self, index):
        secilen = self.sender().currentText()
        print(f"Seçilen öğe: {secilen}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()