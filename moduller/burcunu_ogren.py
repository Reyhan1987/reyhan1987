

def burcunu_ogren():

    dogum_gunu = int(input("Doğum gününüzün sayısını giriniz(GG):"))
    dogum_ayi = int(input("Doğum ayınızın sayısını giriniz(MM): "))
    if (int(dogum_ayi) == 12 and int(dogum_gunu) >= 22) or (
        int(dogum_ayi) == 1 and int(dogum_gunu) <= 19 ):
        print("Oğlak burcusunuz.")
    elif (int(dogum_ayi) == 1 and int(dogum_gunu) >= 20) or (
        int(dogum_ayi) == 2 and int(dogum_gunu) <= 17    ):
        print("Kova burcusunuz.")
    elif (int(dogum_ayi) == 2 and int(dogum_gunu) >= 18) or (
        int(dogum_ayi) == 3 and int(dogum_gunu) <= 19 )   :
        print("Balık burcusunuz.")
    elif (int(dogum_ayi) == 3 and int(dogum_gunu) >= 20) or (
        int(dogum_ayi) == 4 and int(dogum_gunu) <= 19    ):
        print("Koç burcusunuz.")
    elif (int(dogum_ayi) == 4 and int(dogum_gunu) >= 20) or (
        int(dogum_ayi) == 5 and int(dogum_gunu) <= 20    ):
        print("Boğa burcusunuz.")
    elif (int(dogum_ayi) == 5 and int(dogum_gunu) >= 21) or (
        int(dogum_ayi) == 6 and int(dogum_gunu) <= 20    ):
        print("İkizler burcusunuz.")
    elif (int(dogum_ayi) == 6 and int(dogum_gunu) >= 21) or (
        int(dogum_ayi) == 7 and int(dogum_gunu) <= 22    ):
        print("Yengeç burcusunuz.")
    elif (int(dogum_ayi) == 7 and int(dogum_gunu) >= 23) or (
        int(dogum_ayi) == 8 and int(dogum_gunu) <= 22    ):
        print("Aslan burcusunuz.")
    elif (int(dogum_ayi) == 8 and int(dogum_gunu) >= 23) or (
        int(dogum_ayi) == 9 and int(dogum_gunu) <= 22    ):
        print("Başak burcusunuz.")
    elif (int(dogum_ayi) == 9 and int(dogum_gunu) >= 23) or (
        int(dogum_ayi) == 10 and int(dogum_gunu) <= 22    ):
        print("Terazi burcusunuz.")
    elif (int(dogum_ayi) == 10 and int(dogum_gunu) >= 23) or (
        int(dogum_ayi) == 11 and int(dogum_gunu) <= 21    ):
        print("Akrep burcusunuz.")
    elif (int(dogum_ayi) == 11 and int(dogum_gunu) >= 22) or (
        int(dogum_ayi) == 12 and int(dogum_gunu) <= 21    ):
        print("Yay burcusunuz.")

    burcunu_ogren()
burcunu_ogren()