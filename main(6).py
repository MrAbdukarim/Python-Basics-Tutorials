# lang = input("Tilni tanlang (uz/en): ")
#
# if lang == "uz":
#     print("Assalomu alaykum")
# elif lang == "en":
#     print("Hello Mister or Madam")
# else:
#     print("uz va en lardan birini tanlang!")

from random import randint

a = randint(1, 500)
b = randint(1, 500)

c = int(input('{} + {} = '.format(a, b)))

if c == (a + b):
    print("To'g'ri")
else:
    print("Noto'g'ri")

# Topshiriq
year = int(input("Yilni kiriting: "))


if year % 400 !=0 :
    print("Siz kiritgan yil Kabisa yili")
else:
    print("Siz kiritgan yil Kabisa yili emas!")