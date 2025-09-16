import json
import os

DOSYA_ADI="ogrenciler.json"


if not os.path.exists(DOSYA_ADI):
    with open(DOSYA_ADI, "w", encoding="utf-8") as f: 
         json.dump([], f)


def ogrencileri_oku():
    with open (DOSYA_ADI, "r", encoding="utf-8") as f: 
        return json.load(f)
         
    
def ogrencileri_kaydet(ogrenciler):
     with open(DOSYA_ADI,"w", encoding="utf-8") as f:
          json.dump(ogrenciler, f, indent=4,ensure_ascii=False)
    

def ogrenci_ekle():
    ad=input("Öğrenci Adı: ")
    soyad=input("Öğrencinin Soyadı: ")
    numara=input("Öğrenci Numarası: ")
    bolum=input("Bölüm: ")

    ogrenciler=ogrencileri_oku

    for ogr in ogrenciler:  
        if ogr["numara"]==numara:
            print("Bu numaraya sahip öğrenci zaten kayıtlı") 
            return
    
    ogrenciler.append({"ad":ad, "soyad":soyad,"numara":numara,"bolum":bolum,"notlar":{}})
    ogrencileri_kaydet(ogrenciler)
    print("Öğrenci başarıyla eklendi.")


def ogrencileri_listele():
    ogrenciler=ogrencileri_oku
    if not ogrenciler:
         print("Kayıtlı öğrenci yok")
    else:
        print("\n\n----Öğrenci Listesi----")
        for ogr in ogrenciler:
            print(f"Ad:{ogr["ad"]}{ogr["soyad"]} Numara:{ogr["numara"]} Bölüm:{ogr["bolum"]}")

def ogrenci_sil():
    numara=input("Silmek istediğiniz öğrencinin numarası: ")
    ogrenciler=ogrencileri_oku
    yeni_liste=[ogr for ogr in ogrenciler if ogr["numara"]!= numara]

    if len(yeni_liste)==len(ogrenciler):
        print("Bu numaraya sahip öğrenci bulunamadı")
        return
    ogrencileri_kaydet(yeni_liste)
    print("Öğrenci silindi.")


def ogrenci_ara():
    aranan=input("Aramak istediğiniz Ad, Soyad, Numara veya Bölüm: ")
    ogrenciler=ogrencileri_oku
    sonuc=[ogr for ogr in ogrenciler if aranan.lower() in ogr["ad"].lower() 
           or aranan.lower() in ogr["soyad"].lower() 
           or aranan.lower() in ogr["numara"].lower() 
           or aranan.lower() in ogr["bolum"].lower()]
    if not sonuc:
        print("Eşleşen öğrenci bulunamadı")
    else:
        print("\n----Arama Sonuçları----")
        for ogr in sonuc:
            print(f"Ad: {ogr["ad"]}{ogr["soyad"]} Numara:{ogr["numara"]} Bölüm:{ogr["bolum"]}")


def ogrenci_guncelle():
    numara=input("Güncellemek istediğiniz öğrencinin numarası: ")
    ogrenciler=ogrencileri_oku()

    for ogr in ogrenciler:
        if ogr["numara"]==numara:
            print(f"Güncelleniyor:{ogr["ad"]} {ogr["soyad"]} - {ogr[numara]} - {ogr["bolum"]}")
            yeni_ad=input(f"Yeni Ad(Boş bırakılırsa aynı kalır.)[{ogr["ad"]}]: ") or ogr["ad"]
            yeni_soyad=input(f"Yeni Soyad(Boş bırakılırsa aynı kalır.)[{ogr["soyad"]}]: ") or ogr["soyad"]
            yeni_bolum=input(f"Yeni Bölüm(Boş bırakılırsa aynı kalır.)[{ogr["bolum"]}]: ") or ogr["bolum"]
            ogr["ad"]=yeni_ad
            ogr["soyad"]=yeni_soyad
            ogr["bolum"]=yeni_bolum
            ogrencileri_kaydet(ogrenciler)
            print("Öğrenci bilgileri güncellendi.")
            return
    
    print("Bu numaraya sahip öğrenci bulunamadı")

def not_ekle():
    numara=input("Not eklemek istediğiniz öğrencinin numarası: ")
    ogrenciler=ogrencileri_oku()
    
    for ogr in ogrenciler:
        if ogr["numara"]==numara:
            ders=input("Ders adı: ") 
            try:
                not_degeri=float(input("Not: "))
            except ValueError:
                print("Geçerli bir sayı giriniz.")
                return
            
            if ders not in ogr["notlar"]:
                ogr["notlar"][ders]=[] 
                ogr["notlar"][ders].append(not_degeri)
                ogrencileri_kaydet(ogrenciler)
                print("Not eklendi.")
                return
    print("Bu numaraya sahip öğrenci bulunamadı.")

def notlari_listele():
    numara=input("Notlarını görmek istediğiniz öğrencinin numarası: ")
    ogrenciler=ogrencileri_oku

    for ogr in ogrenciler:
        if ogr ["numara"]==numara:
            if not ogr["notlar"]:
                print("Bu öğrencinin hiç notu yok.")
                return
            print(f"\n----{ogr["ad"]}{ogr["soyad"]} Notları----")
            for ders, notlar in ["notlar"].items():
                ort=sum(notlar)/len(notlar)
                print(f"{ders}:{notlar} Ortalama:{ort:.2f}")
            return
    
    print("Bu numaraya sahip öğrenci bulunamadı")



def menu():

    while True:
        os.system("cls")
        print("\n----Öğrenci Kayıt Sistemi----\n")
        print("1- Öğrenci Ekle")
        print("2- Öğrenci Listele")
        print("3- Öğrenci Sil")
        print("4- Öğrenci Ara")
        print("5- Öğrenci Güncelle")
        print("6- Not Ekle")
        print("7- Notları Listele")
        print("8- Çıkış")

        secim=(input("Seçiminiz:"))

        if secim=="1":
            ogrenci_ekle()
        elif secim=="2":
            ogrencileri_listele()
        elif secim=="3":
            ogrenci_sil()
        elif secim=="4":
            ogrenci_ara()
        elif secim=="5":
            ogrenci_guncelle()
        elif secim=="6":
            not_ekle()
        elif secim=="7":
            notlari_listele()
        elif secim=="8":
            print("Programdan çıkılıyor..")
            break
        else:
            print("Geçersiz seçim. Lütfen 1 ile 8 arasında bir değer giriniz.")

    menu()
menu()
            











