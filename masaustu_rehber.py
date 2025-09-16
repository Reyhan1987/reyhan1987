import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox
)
from PyQt5.QtCore import Qt

DATA_FILE = "rehber.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

class TelefonRehberi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📒 Telefon Rehberi")
        self.setGeometry(200, 200, 600, 400)

        self.rehber = load_data()

        self.initUI()
        self.load_table()

    def initUI(self):
        layout = QVBoxLayout()

        # 🔹 Ekleme alanı
        form_layout = QHBoxLayout()
        self.entry_name = QLineEdit()
        self.entry_name.setPlaceholderText("İsim")
        self.entry_phone = QLineEdit()
        self.entry_phone.setPlaceholderText("Telefon")
        self.entry_email = QLineEdit()
        self.entry_email.setPlaceholderText("Email")

        self.btn_add = QPushButton("➕ Ekle")
        self.btn_add.clicked.connect(self.add_contact)

        self.btn_update = QPushButton("✏️ Düzenle")
        self.btn_update.clicked.connect(self.update_contact)

        form_layout.addWidget(self.entry_name)
        form_layout.addWidget(self.entry_phone)
        form_layout.addWidget(self.entry_email)
        form_layout.addWidget(self.btn_add)
        form_layout.addWidget(self.btn_update)

        layout.addLayout(form_layout)

        # 🔹 Arama alanı
        search_layout = QHBoxLayout()
        self.entry_search = QLineEdit()
        self.entry_search.setPlaceholderText("Ara (isim gir)")
        self.entry_search.textChanged.connect(self.search_contact)

        search_layout.addWidget(QLabel("🔍 Ara:"))
        search_layout.addWidget(self.entry_search)

        layout.addLayout(search_layout)

        # 🔹 Tablo
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["İsim", "Telefon", "Email"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)  # doğrudan düzenleme yok
        self.table.setSelectionBehavior(self.table.SelectRows)
        layout.addWidget(self.table)

        # 🔹 Silme butonu
        self.btn_delete = QPushButton("🗑️ Seçili Kişiyi Sil")
        self.btn_delete.clicked.connect(self.delete_contact)
        layout.addWidget(self.btn_delete)

        self.setLayout(layout)

    def load_table(self):
        self.table.setRowCount(0)
        for i, (isim, info) in enumerate(self.rehber.items()):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(isim))
            self.table.setItem(i, 1, QTableWidgetItem(info["telefon"]))
            self.table.setItem(i, 2, QTableWidgetItem(info["email"]))

    def add_contact(self):
        isim = self.entry_name.text().strip()
        telefon = self.entry_phone.text().strip()
        email = self.entry_email.text().strip()

        if not isim or not telefon:
            QMessageBox.warning(self, "Uyarı", "İsim ve telefon zorunludur!")
            return

        if isim in self.rehber:
            QMessageBox.warning(self, "Uyarı", "Bu isim zaten kayıtlı!")
            return

        self.rehber[isim] = {"telefon": telefon, "email": email}
        save_data(self.rehber)
        self.load_table()

        self.entry_name.clear()
        self.entry_phone.clear()
        self.entry_email.clear()

    def update_contact(self):
        secili = self.table.currentRow()
        if secili < 0:
            QMessageBox.warning(self, "Uyarı", "Düzenlemek için bir kişi seçin.")
            return

        isim = self.table.item(secili, 0).text()
        yeni_isim = self.entry_name.text().strip() or isim
        yeni_telefon = self.entry_phone.text().strip() or self.rehber[isim]["telefon"]
        yeni_email = self.entry_email.text().strip() or self.rehber[isim]["email"]

        # Eski kaydı sil, yenisini ekle
        if isim in self.rehber:
            del self.rehber[isim]
        self.rehber[yeni_isim] = {"telefon": yeni_telefon, "email": yeni_email}
        save_data(self.rehber)

        self.load_table()
        self.entry_name.clear()
        self.entry_phone.clear()
        self.entry_email.clear()

        QMessageBox.information(self, "Başarılı", f"{isim} güncellendi.")

    def delete_contact(self):
        secili = self.table.currentRow()
        if secili < 0:
            QMessageBox.warning(self, "Uyarı", "Silmek için bir kişi seçin.")
            return

        isim = self.table.item(secili, 0).text()
        cevap = QMessageBox.question(self, "Onay", f"{isim} silinsin mi?",
                                     QMessageBox.Yes | QMessageBox.No)
        if cevap == QMessageBox.Yes:
            if isim in self.rehber:
                del self.rehber[isim]
                save_data(self.rehber)
                self.load_table()
                QMessageBox.information(self, "Bilgi", f"{isim} silindi.")

    def search_contact(self):
        aranan = self.entry_search.text().lower()
        for i in range(self.table.rowCount()):
            isim = self.table.item(i, 0).text().lower()
            self.table.setRowHidden(i, aranan not in isim)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = TelefonRehberi()
    pencere.show()
    sys.exit(app.exec_())
