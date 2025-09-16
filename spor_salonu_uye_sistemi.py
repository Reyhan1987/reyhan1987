import json
import os

DOSYA_ADI="uye_sistemi.json"

def sistemi_yukle():
    if os.path.exists(DOSYA_ADI):
        with open(DOSYA_ADI,"r",encoding="utf-8") as f:
            return json.load(f)
    return{}

def sistemi_kaydet(uye_sistemi):
    with open(DOSYA_ADI,"w",encoding="utf-8") as f:
        json.dump(uye_sistemi, f, ensure_ascii=False, indent=4)

uye_sistemi=sistemi_yukle()

def kisi_ekle():
    isim=input("\nİsim ve Soyisim giriniz: ")
    if isim in uye_sistemi:
        print("\nBu üye zaten kayıtlı.")
    else:
        telefon=input("Telefon numarası: ")
        uye_sistemi[isim]=telefon
        sistemi_kaydet(uye_sistemi)
        print(f"\n{isim} sisteme eklendi.")
    input()


def kisi_ara():
    isim=input("\nAramak istediğiniz İsim ve Soyisimi giriniz: ")
    if isim in uye_sistemi:
        print(f"{isim} -> {uye_sistemi[isim]}")
    else:
        print("\nÜye bulunamadı.")
    input()


def kisi_sil():
    isim=input("Silmek istediğiniz İsim ve Soyisimi giriniz: ")
    if isim in uye_sistemi:
        del uye_sistemi[isim]
        sistemi_kaydet(uye_sistemi)
        print(f"\n{isim} silindi.")
    else:
        print("\nÜye bulunamadı.")
    input()

def tum_kisileri_listele():
    if not uye_sistemi:
        print("\nÜye yok.")
    else:
        print("\n---Tüm Üyeler---")
        for isim, telefon in uye_sistemi.items():
            print(f"\n{isim} -> {telefon}")
    input()

def menu():
    while True:
        os.system('cls')

        print("\n\n---Spor Salonu Üye Sistemi---\n\n")
        print("1-Üye Ekle")
        print("2-Üye Ara")
        print("3-Üye Sil")
        print("4-Tüm Üyeleri Listele")

        secim=input("Seçiminiz Nedir?: ")

        if secim=="1":
            kisi_ekle()
        elif secim=="2":
            kisi_ara()
        elif secim=="3":
            kisi_sil()
        elif secim=="4":
            tum_kisileri_listele()
        else:
            print("\nGeçersiz seçim")
        input("\nDevam etmek için enter a basınız.")
menu()




