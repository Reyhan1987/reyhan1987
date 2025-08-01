def oyunlar():

    print("\033[1;32;40m")
    print("╔═════════════════════════════════════════╗")
    print("║                                         ║")
    print("║           OYUNLAR                       ║")
    print("║                                         ║")
    print("║   1-Şekil Çizdirme                      ║")
    print("║   2-Sayi Tahmin Oyunu                   ║")
    print("║                                         ║")
    print("║                                         ║")    
    print("║     Seciminiz nedir?                    ║")
    print("╚═════════════════════════════════════════╝")
    s=int(input("Seciminiz nedir?"))
    
    if s==1:
        import moduller.sekil_cizme
        moduller.sekil_cizme()
    
    elif s==2:
        import moduller.sayi_tahmin
        moduller.sayi_tahmin()
    
       
    oyunlar()

oyunlar()