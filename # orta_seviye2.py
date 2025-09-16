# # # orta_seviye2.py
# import random

# liste1 = []
# print(liste1)
# sayiadedi = 1000000
# for a in range(sayiadedi):
#     liste1.append(random.randint(10000,99999))
#     aranan = int(input("Aradığınız sayı nedir?"))
# # a = 0
# # b = 0
# # for b in liste1:
# #     for gg in range(1000000):
# #         a += 1
# #         if b == aranan :   
# #             b += 1     
# #             print (f"sayı {a}.sırada bulundu" )


# bolmesayisi = 2
# baslangic = 0
# bitis = sayiadedi // bolmesayisi 
# kackezbakti = 0
# for gg in range(bolmesayisi):
#     for gg in range(baslangic+2,bitis-2):
#         kackezbakti += 1
#         a += 1
#         if liste1[gg] == aranan :   
#             b += 1     
#             print (f"sayı {a}.sırada bulundu" )
#             break
#     baslangic += sayiadedi // bolmesayisi
#     bitis += sayiadedi // bolmesayisi
# # print(f"{aranan} sayısından {b} adet bulundu.")    
# print(f"{aranan} sayısı {kackezbakti}.kerede bulundu.")    
    
# x = 'print(55+5)'
# eval(x)

# x = input("Bir python komutu girin: ")
# eval(x)
# eval(input())

araclar1 = ["ferrari","Doğan","bmw"] # en çok kullanılan collection 
araclar2 = ("Şahin","TOGG","Ford") # değiştirilemez 
araclar3 = {"Mazda","Volvo","Mercedes"} # set. indexi yok
araclar4 = {"Kıvanç":"Hundai","Uğurhan":"Mercedes","Ahmet":"Honda"} # index yerine key var

print(type(araclar1))
print(type(araclar2))
print(type(araclar3))
print(type(araclar4))

print(araclar1)
print(araclar2)
print(araclar3)
print(araclar4)

print(araclar1[1])
print(araclar2[1])
# print(araclar3[1])
print(araclar4["Ahmet"])

araclar1 += ["Volvo"]
print(araclar1)

# araclar2 += ("Volvo")
# print(araclar2)

# araclar3 += {"Volvo"}
# print(araclar3)
araclar4 += {"Erdinç":"Volvo"}
print(araclar4)