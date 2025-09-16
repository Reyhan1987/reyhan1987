import mysql.connector

def get_students_from_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="okul"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT id, ad_soyad, yas, bolum FROM ogrenciler")
    students = cursor.fetchall()  # Liste olarak al
    connection.close()
    return students

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

class StudentTable(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Öğrenci Listesi")
        self.setGeometry(100, 100, 500, 300)

        # Layout oluştur
        layout = QVBoxLayout()

        # QTableWidget oluştur (4 sütunlu)
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Ad Soyad", "Yaş", "Bölüm"])

        # Verileri tabloya ekle
        students = [
            (1, "Ali Yılmaz", 20, "Bilgisayar Müh."),
            (2, "Ayşe Kaya", 22, "Makine Müh."),
            (3, "Mehmet Demir", 21, "Elektrik-Elektronik Müh."),
            (4, "Zeynep Arslan", 23, "İnşaat Müh.")
        ]
        self.populate_table(students)

        # Tabloyu layout'a ekle
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

    def populate_table(self, students):
        """Öğrenci listesini tabloya ekler"""
        self.tableWidget.setRowCount(len(students))  # Satır sayısını belirle

        for row, student in enumerate(students):
            for col, data in enumerate(student):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(data)))

# PyQt6 uygulamasını başlat
app = QApplication(sys.argv)
window = StudentTable()
window.show()
sys.exit(app.exec())