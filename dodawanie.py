podreczniki = []

## tytuly podrecznikow (trzeba dodac wiecej rodzaji i przedmiotow)

tytuly = {
    "polski": {
        "Nowe ponad słowami": 40,
        "Ponad słowami": 30
    },

    "angielski": {
        "4Minds (poziom A2)": 40,
        "4Minds (poziom B1)": 42,
        "4Minds (poziom B2)": 44
    },

    "niemiecki": {
        "Perfect": 35,
        "Perfect Rozserzony": 30,
    },

    "matematyka": {
        "Nowa MATeMAtyka": 45,
        "MaTeMAtyka": 35,
        "Nowa MATeMAtyka (Poziom rozserzony)": 50,
        "MaTeMAtyka (Poziom rozserzony)": 40
    }
}

# opcja wyboru przedmiotu

def wybierz_przedmiot():
    print("\nWybierz przedmiot:")
    print("1 - Polski")
    print("2 - Angielski")
    print("3 - Niemiecki")
    print("4 - Matematyka")

    wybor = input("Wybierz numer: ")

    if wybor == "1":
        return "polski"
    elif wybor == "2":
        return "angielski"
    elif wybor == "3":
        return "niemiecki"
    elif wybor == "4":
        return "matematyka"
    else:
        print("Blad")
        return None

def wybierz_podrecznik(przedmiot):
    print("\nWybierz podrecznik: ")

    lista = list(tytuly[przedmiot])

    for i, tytul in enumerate(lista, 1):
        print(i, "-", tytul, "-", tytuly[przedmiot][tytul], "zł")

    wybor = int(input("Wybierz numer: "))

    return lista[wybor - 1]

def dodaj_podrecznik():
    print("\nDodawanie")

    przedmiot = wybierz_przedmiot()

    if przedmiot is None:
        return
    tytul = wybierz_podrecznik(przedmiot)

    print("\nWybierz klase")
    print("1 - klasa 1")
    print("2 - klasa 2")
    print("3 - klasa 3")
    print("4 - klasa 4")
    print("5 - klasa 5")

    klasa = input("Twoja klasa: ")

    print("")
    print("1 - Podręcznik")
    print("2 - Cwiczenia")

    wybor = input("Wybierz rodzaj ksiazki: ")

    if wybor == "1":
        rodzaj = "podrecznik"
    elif wybor == "2":
        rodzaj = "cwiczenia"
    else:
        print("blad (nieprawidlowy wybor)")
        return

    cena = tytuly[przedmiot][tytul]

    ksiazka = {
        "tytul": tytul,
        "przedmiot": przedmiot,
        "klasa": klasa,
        "rodzaj": rodzaj,
        "cena": cena
    }

    podreczniki.append(ksiazka)

    print("")
    print(rodzaj.title(), "zostal dodany")
    print("Cena", cena, "zł")
    print("----------")

# menu (dodawanie ksiazek lub koniec)

def menu():
    while True:
        print("\nZakup ksiazke")
        print("1 - dodaj")
        print("2 - koniec")

        wybor = input("Wybierz opcje ")

        if wybor == "1":
            dodaj_podrecznik()

        elif wybor == "2":
            print("koniec")
            break

        else:
            print("blad (nieprawidlowy wybor)")
menu()
