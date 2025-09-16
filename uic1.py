import sys, os; from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

class GirisEkrani(QDialog):  # QMainWindow yerine QDialog kullan!
    def __init__(self):
        super().__init__()
        # .ui dosyasının tam yolu
        klasor = r"E:\aErdinc\IS\Projeler\CALISILANDenemeDersOrnek\Python\Learn PYTHON_Python OGREN\07_python_masaustu_programlama\QtDesigner"
        ui_dosyasi = os.path.join(klasor, "giris.ui")
        # .ui dosyasını yükle
        uic.loadUi(ui_dosyasi, self)
       
        # Giriş butonuna tıklama olayını bağla
        self.pushButton_1.clicked.connect(self.kontrolet)
   
    def kontrolet(self):
        # Kullanıcı adı ve şifreyi al
        kullaniciadi = self.lineEdit_1.text()  # Kullanıcı adı
        sifre = self.lineEdit_2.text()  # Şifre

        # Doğru kullanıcı adı ve şifreleri bir liste olarak tanımla
        dogru_kullanicilar = [
            {"kullaniciadi": "admin", "sifre": "123"},
            {"kullaniciadi": "user1", "sifre": "abc123"},
            {"kullaniciadi": "guest", "sifre": "guest123"}
        ]
       
        # Kullanıcı adı ve şifreyi listeyle kontrol et
        for kullanici in dogru_kullanicilar:
            if kullaniciadi == kullanici["kullaniciadi"] and sifre == kullanici["sifre"]:
                QMessageBox.information(self, "Giriş Başarılı", "Giriş başarılı!")
                return

        # Eğer eşleşen kullanıcı adı ve şifre bulunmazsa
        QMessageBox.warning(self, "Giriş Hatası", "Kullanıcı adı veya şifre hatalı!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GirisEkrani()
    window.show()
    sys.exit(app.exec_())