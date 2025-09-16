import sys 
from PyQt6.QtWidgets import*
# import ticari


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Ekranı")
        central_widget=QWidget()
        layout=QVBoxLayout

        label_username=QLabel("Kullanıcı Adı:")
        self.username_input=QLineEdit()
        layout.addWidget(label_username)
        layout.addWidget(self.username_input)

        label_password=QLabel("Şifre:")
        self.password_input=QLineEdit
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(label_password)
        layout.addWidget(self.password_input)

        login_button=QPushButton("Giriş yap")
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def login(self):
        username=self.username_input.text()
        password=self.password_input.text()

        if username=="admin" and password=="1234":
            self.open_ticari_window.show()
        
        else: QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre")
    
    def open_ticari_window(self):
        QMessageBox.information(self,"Başarılı", "Giriş başarılı. \nAna Programdasınız.")
        self.close()
        self.ticari_window=ticari.TicariWindow()
        self.ticari_window.show()

def main():
    app=QApplication(sys.argv)
    window=LoginWindow()
    window.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()
