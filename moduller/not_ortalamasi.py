vize = float(input("Vize notunu giriniz: "))
proje = float(input("Proje notunu giriniz: "))
final = float(input("Final notunu giriniz: "))
# Ortalama hesapla
ortalama = vize*0.3 + proje*0.3 + final*0.4

if ortalama >= 50:
    sonuc = 'geçti'
else:
    sonuc = 'kaldı'
print("Ortalamanız: ", ortalama)
print("Sonucunuz: ", sonuc)