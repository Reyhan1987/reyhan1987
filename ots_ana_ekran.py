import mysql.connector


try:
  vtb = mysql.connector.connect( # vtb veri tabani baglantisi
    host="localhost", # Server/Veritabanı sistemi (instance) adı.
    user="root", # Veritabanı kullanıcı adı
    password="1234" # Veritabanı sistemi(instance) şifresi
  )
  secilen = vtb.cursor()
  secilen.execute("create database if not exists ots")
  secilen.execute("show databases")
  vtlistesi = secilen.fetchall()
  print("Veritabanları listesi:", vtlistesi)
  print("Bağlantı tamam:")
except:
  print("Veritabanına bağlanırken bir hata oluştu.")


# -------------------------------------
from PyQt6.QtWidgets import *
import ots_ceviri_modul
import ots_ogrenci_kayit_modulu


class AnaPencere(QMainWindow):
    def tiklama(self):
        alert = QMessageBox()
        alert.setText('Tıkladın!')
        alert.exec()


    # def ogrenciEkle(self):
    #     # pencere = ots_ogrenci_kayit_modulu
    #     print("ogrenciEkle çalıştı.")
    #     pencere1 = ots_ogrenci_kayit_modulu.KayitPenceresi()
    #     pencere1.show()
    #     # self.close()
    #     print("ogrenciEkle çalıştı.1")


    def __init__(self):
        super().__init__()
        def ceviriac():
            self.ceviripenceresi = ots_ceviri_modul.ceviriPenceresi()
            self.ceviripenceresi.show()
            # self.close()  


        def ogrenciEkle():
            # pencere = ots_ogrenci_kayit_modulu
            print("ogrenciEkle çalıştı.")
            self.pencere1 = ots_ogrenci_kayit_modulu.KayitPenceresi()
            self.pencere1.show()
            # self.close()
            print("ogrenciEkle çalıştı.1")


        icerik = QVBoxLayout()


        ceviri = QPushButton('Çeviri')
        icerik.addWidget(ceviri)
        ceviri.clicked.connect(ceviriac)


        icerik.addWidget(QPushButton('Dene'))
        buton1 = QPushButton('Tıkla')
        buton1.clicked.connect(self.tiklama)


        ogrenciKayit = QPushButton('Öğrenci ekle')
        icerik.addWidget(ogrenciKayit)
        ogrenciKayit.clicked.connect(ogrenciEkle)


        icerik.addWidget(buton1)
        icerik.addWidget(QLabel('Bilgi'))


        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)


class GirisEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
   
        self.setWindowTitle("... Uygulaması")
        self.setFixedWidth(300)
        self.setFixedHeight(200)


        layout = QVBoxLayout() # layout = QHBoxLayout()
        layout.addWidget(QLabel("Kullanıcı adı:"))
        ka = QLineEdit()
        layout.addWidget(ka)
        layout.addWidget(QLabel("Şifre:"))
        sf = QLineEdit()
        sf.setEchoMode(QLineEdit.EchoMode.Password)


        # sf.echoMode.
        layout.addWidget(sf)
        layout.addWidget(QCheckBox("Beni hatırla"))


        def kontrol():
            secilen.execute("select * from ots.kullanicilar")
            kullanicilistesi = secilen.fetchall()
            print(kullanicilistesi)
            print(ka.text())
            print(sf.text())
            for aa in kullanicilistesi:
                # if ka.text() == "adm" and sf.text() == "123":
                if ka.text() == aa[1] and sf.text() == aa[2]:
                    print ("giris yapabilir")
                    self.anaekran = AnaPencere()
                    self.anaekran.show()
                    self.close()
            else:
                print ("izin yok")
        buton = QPushButton("Giriş yap")
        layout.addWidget(buton)
        buton.clicked.connect(kontrol)
        layout.addWidget(QLabel("..."))


        widget = QWidget()
        widget.setLayout(layout)


        self.setCentralWidget(widget)
        self.show()




aa = QApplication([])
pencere = GirisEkrani()
pencere.show()
aa.exec()
