def dodaj_podrecznik(podreczniki):
    print("\nDODAWANIE PODRĘCZNIKA")

    tytul = input("Tytuł: ")
    klasa = input("Klasa: ")
    przedmiot = input("Przedmiot: ")
    stan = input("Stan (nowy/dobry/używany): ")

    while True:
        try:
            cena = float(input("Cena (zł): "))

            if cena < 0:
                print("Cena nie może być ujemna.")
            else:
                break

        except ValueError:
            print("Podaj poprawną cenę")

    podrecznik = {
        "tytul": tytul,
        "klasa": klasa,
        "przedmiot": przedmiot,
        "stan": stan,
        "cena": cena
    }

    podreczniki.append(podrecznik)

    print("\nPodręcznik został dodany!")
