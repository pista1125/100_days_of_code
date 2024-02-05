import random
import pandas

ertek = [random.randint(0, 200) for x in range(100)]
szazalek = [random.randint(0, 100) for x in range(100)]

darab = [x for x in range(100)]

Text =f'''
                                        Százalékszámítás dolgozat
Név:

1.	Andrisék családja lakásfelújításra {random.choice(ertek)} euró kölcsönt vett föl egy évre.
{random.choice(szazalek)}% kamatot kell fizetni. Mekkora összeget kell visszafizetnie Andris családjának egy év múlva?

2.	Egy vevőnek sikerült {random.choice(ertek)} Forintra lealkudnia {random.choice(ertek)} Forintos áron meghirdetett terméket.
Hány százalékot tudott spórolni a vevő?

3.	Egy nyeregtetős ház tetejére, {random.choice(ertek)} négyzetméter napkollektort szerelnek,
amellyel a teljes tető {random.choice(szazalek)}%-át fedték le. Mekkora a tető teljes felülete?

4.	Számold ki:

a)	a {random.choice(ertek)}-nak a {random.choice(szazalek)}%-a                 b) a {random.choice(ertek)}-nek a {random.choice(szazalek)}%-a                c) a {random.choice(ertek)}-nek a {random.choice(szazalek)}%-a

d)	az {random.choice(ertek)}-nak az {random.choice(szazalek)}%-a               e) a {random.choice(ertek)}-nek a {random.choice(szazalek)}%-a                f) az {random.choice(ertek)}-nek a {random.choice(szazalek)}%-a

5.	Számold ki, hogy hány százaléka?

b)	a {random.choice(ertek)}-nek a {random.choice(ertek)}                       b) a {random.choice(ertek)}-nak a {random.choice(ertek)}                  c) a {random.choice(ertek)}-nek a {random.choice(ertek)}

e)	az {random.choice(ertek)}-nak a {random.choice(ertek)}                      f) a {random.choice(ertek)}-nek a {random.choice(ertek)}                  g) az {random.choice(ertek)}-nak a {random.choice(ertek)}

6.	Határozd meg melyik számnak:

a)	a {random.choice(szazalek)}%-a az {random.choice(ertek)}                     b) a {random.choice(szazalek)}%-a a {random.choice(ertek)}                   c) a {random.choice(szazalek)}%-a a {random.choice(ertek)} 

d)	a {random.choice(szazalek)}%-a a {random.choice(ertek)}                      e) {random.choice(szazalek)}%-a a {random.choice(ertek)}                     f) a {random.choice(szazalek)}%-a a {random.choice(ertek)}

'''

for x in range(20):
    with open(f"my_new_file_{darab[x]}.txt", mode="w") as file:
        file.write(Text)

