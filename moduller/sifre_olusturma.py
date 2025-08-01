import string 
import random

characters = string.ascii_letters + string.digits + string.punctuation

def createPass():
    password = " "
    passwordlenght=int(input("Sifre uzunluğunu giriniz:"))
    for i in range(passwordlenght):
        password+=random.choice(characters)
    print(password)

createPass()
