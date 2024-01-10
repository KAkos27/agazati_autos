from Auto import Auto


def file_belovas():
    vegso_lista = []
    fajl = open("auto.txt", "r", encoding="utf-8")
    fajl.readline()
    lista = fajl.readlines()
    fajl.close()

    for i in range(0, len(lista), 1):
        sor_lista = lista[i].strip()
        sor_lista = sor_lista.split("$")
        auto = Auto(sor_lista[0], sor_lista[1])
        vegso_lista.append(auto)

    return vegso_lista


def flotta(lista):
    print("III/Flotta:")
    print(f"\tAutók száma: {len(lista)}")


def legfiatalabb(lista):
    min_ev = 1000
    legfiatalabb_index = 0
    for i in range(0, len(lista), 1):
        if int(lista[i].datum) > min_ev:
            min_ev = int(lista[i].datum)
            legfiatalabb_index = i

    print("III/Legfiatalabb")
    print(
        f"\tA legfiatalbb autó: {lista[legfiatalabb_index].nev} ({lista[legfiatalabb_index].datum})"
    )


def atlag(lista):
    gyujto = 0
    atlag = 0
    for i in range(0, len(lista), 1):
        gyujto += 2024 - int(lista[i].datum)

    atlag = gyujto / len(lista)
    print("III/Átlag kor")
    print(f"\tAz autók átlagos kora: {atlag} év.")
