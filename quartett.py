# coding=utf-8
from random import randint,shuffle


karten = [
    ('China',1433, 9.6, 13368073),
    ('Indien',1366, 3.3, 2718732),
    ('USA',329, 9.8, 20580250),
    ('Indonesien',270, 1.9, 1022454),
    ('Pakistan',216, 0.8, 314588),
    ('Brasilien',211, 8.5, 1867818),
    ('Nigeria',200, 0.9, 398186),
    ('Bangladesch',163, 0.15, 288424),
    ('Russland',145, 17.1, 1657290),
    ('Mexiko',127, 2.0, 1222053)
]
shuffle(karten)
attr = ['Einwohner','Fläche', 'BIP in $']

k1 = karten[0:5]
k2 = karten[5:10]
amZug = 1


gesehen = []

Einwohner = []
Fläche = []
BIP = []
Happy = []

def zugInfo(k):
    gesehen.append(k)

def zug1(k):
    durchschnitt_1 = 0
    durchschnitt_2 = 0
    durchschnitt_3 = 0
    durchschnitt_4 = 0

    gesehen.append(k)
    Einwohner.append(k[1])
    Fläche.append(k[2])
    BIP.append(k[3])
    Happy.append(k[4])

    for i in range(len(BIP)):
        durchschnitt_1 += Einwohner[i]
        durchschnitt_2 += Fläche[i]
        durchschnitt_3 += BIP[i]
        durchschnitt_4 += Happy[i]

    durchschnitt_1 /= len(BIP)
    durchschnitt_2 /= len(BIP)
    durchschnitt_3 /= len(BIP)
    durchschnitt_4 /= len(BIP)

    if k[1] > durchschnitt_1:
        return 1
    if k[2] > durchschnitt_2:
        return 2
    if k[3] > durchschnitt_3:
        return 3
    if k[4] > durchschnitt_4:
        return 4
    


    return randint(1,3)

def zug2(k):
    return int(input("entscheide dich zwischen 1 und 2 und 3 "))

def zeigeKarte(k):
    print(f"\n--- {k[0]} ---")
    print(f"Einwohner: {k[1]}")
    print(f"Fläche:{k[2]}")
    print(f"BIP: {k[3]:,}\n")


print("\n")
while k1 and k2:
    print("*****************************************************************************\nDu hast noch: ",len(k2)," Karten!")
    karte1 = k1.pop()
    karte2 = k2.pop() 
    zeigeKarte(karte2)

    if amZug == 1:
        wahl1 = zug1(karte1)
    else:
        wahl1 = zug2(karte2)
    print("Zug Spieler 1:", attr[wahl1 - 1], karte1[wahl1])
    print("Spieler 2:", karte2[wahl1])
    if karte1[wahl1] > karte2[wahl1]:
        k1.insert(0,karte1)
        k1.insert(0,karte2)
        amZug = 1
        print("\nZug geht an spieler1\n")
    else:
        k2.insert(0,karte1)
        k2.insert(0,karte2)
        amZug = 2
        print("Karte Gegner")
        zeigeKarte(karte1)
        print("\nZug geht an spieler2\n")

    input("<")

if k1:
    print("Spikler 1 gewinnt")
else:
    print("Spikler 2 gewinnt")
print("\n")
