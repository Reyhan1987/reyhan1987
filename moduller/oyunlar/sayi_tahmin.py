import random as r
print("\n\nSayi Tahmin Oyunu".upper())
min=1
max=100
hak=10
puan=100
tutulan=r.randint(min,max)
print(f"Ben {min} ile {max} arasinda bir sayi tuttum.\n\
      Bunu tahmin eder misin? \n\
      {hak} hakkin var.")
for a in range (hak):
    tahmin=int(input("\nTahminin nedir?"))
    if tahmin==tutulan:
        print("\nAferin, bildin!")
        break
    elif tahmin>tutulan:
        puan-=100//hak
        print(f"\nTahminin tutulan sayidan buyuk.\nPuanin:{puan}")
    elif tahmin<tutulan:
        puan-=100//hak
        print(f"\nTahminin tutulan sayidan kucuk.\nPuanin:{puan}")
print(f"Bitti.\nPuanin{puan}")




