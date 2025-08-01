
def hesap_menu():

    print("\033[1;32;40m")
    print("╔═════════════════════════════════════════╗")
    print("║           HESAP MAKİNESİ                ║")
    print("║                                         ║")
    print("║   1-TOPLAMA                             ║")
    print("║   2-ÇIKARMA                             ║")
    print("║   3-ÇARPMA                              ║")
    print("║   4-BÖLME                               ║")
    print("║                                         ║")    
    print("║     Seciminiz nedir?                    ║")
    print("╚═════════════════════════════════════════╝")
    s=int(input("Seciminiz nedir?"))
    
    
    if s==1:
        sayi1=int(input("1.sayiyi girin:"))
        sayi2=int(input("2.sayiyi girin:"))
        toplam=sayi1+sayi2
        print(f"\n\nToplam:{toplam}")
   
    elif s==2:
        eksilen=int(input("Eksilen sayıyı girin:"))
        cikan=int(input("Çıkan sayıyı girin:"))
        cikarma=eksilen-cikan
        print(f"\n\nÇıkarma:{cikarma}")
              
    elif s==3:
        sayi1=int(input("1.sayıyı girin:"))
        sayi2=int(input("2.sayıyı girin:"))
        carpim=sayi1*sayi2
        print(f"\n\nÇarpma:{carpim}")
    
    elif s==4:
        bolunen=int(input("Bölünen sayıyı girin:"))
        bolen=int(input("Bölen sayıyı girin:"))
        bolum=bolunen/bolen
        print(f"\n\nBölüm:{bolum}")
    
     
    hesap_menu()

hesap_menu()