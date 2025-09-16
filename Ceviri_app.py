from PyQt6.QtWidgets import*

uygulama=QApplication ([])
pencere=QMainWindow()
pencere.setWindowTitle("Çeviri")

içerik=QVBoxLayout()
içerik.addWidget(QLabel("Kullanıcı adı:"))
içerik.addWidget(QLineEdit(""))
içerik.addWidget(QLabel("Şifre:"))
içerik.addWidget(QLineEdit())

dugmeler=QHBoxLayout()
dugmeler.addWidget(QPushButton("Giriş yap"))
dugmeler.addWidget(QPushButton("Vazgeç"))
dugmeler.addWidget(QPushButton("Çıkış"))

içerik.addLayout(dugmeler)
araclar=QWidget()
araclar.setLayout(içerik)
pencere.setCentralWidget(araclar)
pencere.show()

uygulama.exec()





