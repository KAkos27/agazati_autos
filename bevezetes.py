def elso_feladat():
    print("I/A")
    auto_nev: str = str(input("Autó neve: "))
    gyartas_datum: int = int(input("Gyártás dátum: "))
    print("I/B")

    if gyartas_datum == 2024:
        print(f"\tEz a(z) {auto_nev} friss gyártás")
    elif gyartas_datum < 2000:
        print(f"\tEz a(z) {auto_nev} öreg autó")
    else:
        print(f"\tEz a(z) {auto_nev} átlagos korú")
