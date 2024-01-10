import math
import random


def szam_gen():
    print("II/A, B, C:")
    szam_lista = []
    lista_szoveg: str = ""
    for i in range(0, 5, 1):
        szam: int = math.floor(random.random() * 90 + 1)
        if i < 4:
            lista_szoveg += str(szam) + ";"
        else:
            lista_szoveg += str(szam)
    print("\t" + lista_szoveg)
    szam_lista.append(lista_szoveg)
    return szam_lista


def egyjegyuek_szama(lista):
    lista = lista[0].split(";")
    egyjegyu_gyujto = 0
    for i in range(0, len(lista), 1):
        if int(lista[i]) < 10:
            egyjegyu_gyujto += 1
    eredmeny: str = f"\tEgyjegyűek száma: {egyjegyu_gyujto}"
    return eredmeny


def konzol_kiir(kiirando):
    print("II/D,E:")
    print(kiirando)


def file_kiir(kiirando):
    fajl = open("szamok.txt", "w", encoding="utf-8")
    fajl.write("II/F:\n")
    fajl.write(kiirando)
    fajl.close()
