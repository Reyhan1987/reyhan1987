import time
print ("\n\nWELCOME.. LET'S LEARN ENGLISH LEVEL WITH 5 QUESTIONS")
time.sleep(1)
print("\n\nAre you ready?")
time.sleep(1)
print("\n\nFirst question is coming...")
time.sleep(1)
puan=0
print("\n\nPlease choose the best option to complete the sentence.\n\nCould you tell me your surname?")
time.sleep(1)
print("1)Would you like me to spell it?")
print("2)Do you like my family name?")
print("3)How do I say that?")
time.sleep(2)
s=int(input("What is your choice?"))
if s==1:
   puan+=10 
if s==2:
   puan+=0
if s==3:
   puan+=0
print(f"\nScore:{puan} point")
print("\n\nPlease choose the best option to complete the sentence.\n\nWho gave you this book, Lucy?")
time.sleep(1)
print("1)I bought it.")
print("2)For my birthday.")
print("3)My uncle was.")
time.sleep(2)
s=int(input("\n\nWhat is your choice?"))
if s==1:
   puan+=0 
if s==2:
   puan+=0
if s==3:
   puan+=10
print(f"\nScore:{puan} point")
print("\n\nPlease choose the best option to complete the sentence.\n\nDo you mind if I come too?")
time.sleep(1)
print("1)That's fine!")
print("2)I'd like to.")
print("3)I don't know if I can.")
time.sleep(1)
s=int(input("\n\nWhat is your choice?"))
if s==1:
   puan+=0 
if s==2:
   puan+=10
if s==3:
   puan+=0
print(f"\nScore:{puan} point")
print("\n\nPlease choose the best option to complete the sentence.\n\nWhen you come to my house,......your camera with you.")
time.sleep(1)
print("1)take")
print("2)show")
print("3)bring")
time.sleep(2)
s=int(input("\n\nWhat is your choice?"))
if s==1:
   puan+=0 
if s==2:
   puan+=0
if s==3:
   puan+=10
print(f"\nScore:{puan} point")
print("\n\nPlease choose the best option to complete the sentence.\n\nPaul arrived at the shop ....... as the manager was closing for the day.")
time.sleep(5)
print("1)even")
print("2)just")
print("3)still")
time.sleep(2)
s=int(input("\n\nWhat is your choice?"))
if s==1:
   puan+=0 
if s==2:
   puan+=10
if s==3:
   puan+=0
print(f"\nScore:{puan} point")
if puan>=40:
    print("\n\nCongratulations! Your Level is Advanced.")
if 40>puan>=30:
    print("\n\nYour Level is Upper.")
if 30>puan>=20:
    print("\n\nYour Level is Intermediate.")
if 20>puan>=10:
    print("\n\nYour Level is Pre-Intermadiate.")
if 10>puan>=0:
    print("\n\nYour Level is Basic.")


