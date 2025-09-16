# # orta_seviye.py

# import turtle as t
# t.speed(100)
# def kare(x):
#     if x < 50 : return x
#     else:
#         for i in range (4):
#             t.forward(x)
#             t.right(90)
#         return kare(x-10)

# aaa = int (input("Karenin uzun kenarı ne kadar?"))
# kare(aaa)
# input()

import random
liste1 = []
print(liste1)
sayiadedi = 1000000
for a in range(sayiadedi):
    liste1.append(random.randint(10000,99999))

print("liste1:")
for x in liste1:
    print(x)