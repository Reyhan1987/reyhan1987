def kitle_indeksi():
    agirlik=int(input("Ağırlığınızı giriniz(kg):"))
    boy=float(input("Boyunuzu giriniz(m):"))
    sonuc=agirlik/(boy*boy)
    
    if 18.5>=sonuc>0:
        print("Zayıfsınız. Kilo almanız sağlıklıdır.")   
    elif 25>=sonuc>18.5:
        print("Sağlıklı kilodasınız.")  
    elif 30>=sonuc>25:
        print("Şişmansınız.")  
    elif 40>=sonuc>30:
        print("Obezsiniz.")  
    elif sonuc>40:
        print("Aşırı obezsiniz.")  

    kitle_indeksi()
kitle_indeksi()
