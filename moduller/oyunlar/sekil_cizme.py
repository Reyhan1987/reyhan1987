
import turtle as t, random as r

def cizim_menu():

    print("\033[1;32;40m")
    print("╔═════════════════════════════════════════╗")
    print("║                                         ║")
    print("║           CİZİM MENU                    ║")
    print("║                                         ║")
    print("║   1-Kare cizdir                         ║")
    print("║   2-Ücgen cizdir                        ║")
    print("║   3-Rastgele sekiller cizdir            ║")
    print("║                                         ║")    
    print("║      Seçiminiz nedir?                   ║")
    print("╚═════════════════════════════════════════╝")
    s=int(input("Seçiminiz nedir?"))
    if s==1:
        kare_ciz()
    elif s==2:
        ucgen_ciz()
    elif s==3:
        rastgele_sekiller()
    
def kare_ciz():
    for a in range(4):
        t.forward(100)
        t.right(90)


def ucgen_ciz():
    for a in range(3):
        t.forward(100)
        t.right(120)


def rastgele_sekiller():
    import random as r, turtle as t
    t.speed(10)
    for b in range(r.randint(5,20)):
        renkler=["red","green","blue","yellow"]
        ku=r.randint(50,150)
        x=r.randint(-300,300)
        y=r.randint(-300,300)
        t.color(r.choice(renkler))
        t.up()
        t.goto(x,y)
        t.down()
        ks=r.randint(3,8)
        for a in range(ks):
            t.forward(ku)
            t.right(360/ks)
    
    cizim_menu()
cizim_menu()






