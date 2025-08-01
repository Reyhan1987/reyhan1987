
def uygulamalar():

    print("\033[1;32;40m")
    print("╔═════════════════════════════════════════╗")
    print("║                                         ║")
    print("║       FAYDALI UYGULAMALAR               ║")
    print("║                                         ║")
    print("║   1-Hesap Makinesi                      ║")
    print("║   2-Emeklilik Hesaplama                 ║")
    print("║   3-Şifre Oluşturma                     ║")
    print("║   4-Takvim                              ║")
    print("║   5-Sicaklik Çevirme                    ║")
    print("║   6-Not Ortalamasi Hesaplama            ║")
    print("║   7-Sağlikli Kitle İndeksi Hesaplama    ║")
    print("║   8-Burcunu Öğren                       ║")
    print("║   9-Oyunlar                             ║")
    print("║   10-Learn English Level                ║") 
    print("║                                         ║")   
    print("║      Seçiminiz nedir?                   ║")
    print("╚═════════════════════════════════════════╝")
    s=int(input("Seçiminiz nedir?"))
    if s==1:
        import moduller.hesap_makinesi
        moduller.hesap_makinesi.hesap_menu()
    if s==2:
        import moduller.emeklilik_hesaplama.emeklilik_hesaplama 
        moduller.emeklilik_hesaplama.emeklilik_hesaplama()
    if s==3:
       import moduller.sifre_olusturma
       moduller.sifre_olusturma()
    if s==4:
        import moduller.takvim
        moduller.takvim()      
    if s==5:
        import moduller.sicaklik_cevirme
        moduller.sicaklik_cevirme()
    if s==6:
        import moduller.not_ortalamasi
        moduller.not_ortalamasi()
    if s==7:
       import moduller.kitle_indeksi
       moduller.kitle_indeksi()
    if s==8:
        import moduller.burcunu_ogren
        moduller.burcunu_ogren()
    if s==9:
        import moduller.oyunlar.oyunlar
        moduller.oyunlar.oyunlar()
    if s==10:
        import moduller.english_level
        moduller.english_level()
      
    uygulamalar()

uygulamalar()