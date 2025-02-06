import sys
import random
import string
from PyQt5 import uic, QtWidgets

def generate_temp_mail():
    domains = ['@gmail.com', '@outlook.com', '@russ_aka.com']
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return username + random.choice(domains)

class TempMailApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui.ui", self)
        
        self.bt1.clicked.connect(self.generate_email)
        self.bt2.clicked.connect(self.clear_email)
        self.bt3.clicked.connect(self.save_email)
    
    def generate_email(self):
        self.le.setText(generate_temp_mail())
    
    def clear_email(self):
        self.le.clear()
    
    def save_email(self):
        email = self.le.text()
        if email:
            with open("fichier.txt", "w") as file:
                file.write(email + "\n")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TempMailApp()
    window.show()
    sys.exit(app.exec())
