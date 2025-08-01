import datetime
import time
def erkek_emeklilik():

    print("\033[1;32;40m")
    print("╔═════════════════════════════════════════╗")
    print("║        ERKEK EMEKLİLİK HESAPLAMA        ║")
    print("║                                         ║")
    print("║   1-YAŞ KRİTERİ                         ║")
    print("║   2-SİGORTA BAŞLANGIÇ KRİTERİ           ║")
    print("║   3-PRİM SAYISI KRİTERİ                 ║")    
    print("║                                         ║")    
    print("║     Seçiminiz nedir?                    ║")
    print("╚═════════════════════════════════════════╝")
    s=int(input("Seçiminiz nedir?"))
    if s==1:
        yas_kriteri()
            
    elif s==2:
        sigorta_baslangic()
    
    elif s==3:
        prim_sayisi()

def yas_kriteri():
    
    dogum_yil=int(input("Doğum yılınızı giriniz(YYYY):"))
    guncel_tarih=datetime.datetime.now()
    guncel_yil=guncel_tarih.year
    yas=guncel_yil-dogum_yil
    print("Sen:",yas,"yaşındasın.")
    time.sleep(1)
    if yas-60>=0:
        print("Yaş kriterini sağlıyorsunuz")
    elif yas-60<=0:
        print("Yaş kriterini sağlamıyorsunuz")

def sigorta_baslangic():
    baslangic=int(input("Sigorta başlangıç yılınız nedir?"))
    guncel_tarih=datetime.datetime.now()
    guncel_yil=guncel_tarih.year
    year=guncel_yil-baslangic
    print("Sigortanız başlayalı",year,"olmuş.")
    if year-25>=0:
        print("Sigorta başlangıç kriterini sağlıyorsunuz")
    elif year-25<=0:
        print("Sigorta baslangıç kriterini sağlamıyorsunuz") 

def prim_sayisi():
    ay_sayisi=int(input("Sigorta priminiz kaç ay ödendi?"))
    prim=ay_sayisi*30
    print("Sigorta prim sayınız:",prim,"gündür.")
    if prim-4500>=0:
        print("Tebrikler! Prim sayısı yeterlidir.")
    elif prim-4500<=0:
        print("Prim sayısı yetersizdir.")
    

    erkek_emeklilik()

erkek_emeklilik()