# Kadın için 58, erkek için 60 yaşını doldurmak ve 25 yıldan beri sigortalı bulunmak ve en az 4500 gün prim ödemiş olmak.Bir ay 30 prim günü

import datetime
def emeklilik_menu():

    print("\033[1;32;40m")
    print("╔═════════════════════════════════════════╗")
    print("║        EMEKLİLİK HESAPLAMA              ║")
    print("║                                         ║")
    print("║   1-KADIN EMEKLİLİK                     ║")
    print("║   2-ERKEK EMEKLİLİK                     ║")
    print("║                                         ║")    
    print("║     Cinsiyetiniz nedir?                 ║")
    print("╚═════════════════════════════════════════╝")
    s=int(input("Cinsiyetiniz nedir?"))
    if s==1:
        import emeklilik_hesaplama.kadin_emeklilik
        emeklilik_hesaplama.kadin_emeklilik()
                
    elif s==2:
        import emeklilik_hesaplama.erkek_emeklilik
        emeklilik_hesaplama.erkek_emeklilik()
        

    emeklilik_menu()

emeklilik_menu()