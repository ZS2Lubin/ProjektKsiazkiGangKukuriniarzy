podreczniki = []


def dodaj_podrecznik():
    print("\n--- DODAWANIE PODRĘCZNIKA ---")

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
            print("Podaj poprawną cenę, np. 25.50")

    podrecznik = {
        "tytul": tytul,
        "klasa": klasa,
        "przedmiot": przedmiot,
        "stan": stan,
        "cena": cena
    }

    podreczniki.append(podrecznik)

    print("\nPodręcznik został dodany!")


def wyswietl_podreczniki(lista=None):
    print("\n--- DOSTĘPNE PODRĘCZNIKI ---")

    if lista is None:
        lista = podreczniki

    if len(lista) == 0:
        print("Brak dostępnych podręczników.")
        return

    for i, podrecznik in enumerate(lista, start=1):
        print(f"\n[{i}]")
        print(f"Tytuł: {podrecznik['tytul']}")
        print(f"Klasa: {podrecznik['klasa']}")
        print(f"Przedmiot: {podrecznik['przedmiot']}")
        print(f"Stan: {podrecznik['stan']}")
        print(f"Cena: {podrecznik['cena']:.2f} zł")


def wyszukaj_podrecznik():
    print("\n--- WYSZUKIWANIE ---")

    fraza = input(
        "Wpisz tytuł, klasę lub przedmiot, którego szukasz: "
    ).lower()

    wyniki = []

    for podrecznik in podreczniki:
        if (
            fraza in podrecznik["tytul"].lower()
            or fraza in podrecznik["klasa"].lower()
            or fraza in podrecznik["przedmiot"].lower()
        ):
            wyniki.append(podrecznik)

    if len(wyniki) == 0:
        print("\nNie znaleziono żadnych podręczników.")
    else:
        print(f"\nZnaleziono: {len(wyniki)} podręcznik(ów).")
        wyswietl_podreczniki(wyniki)


def usun_podrecznik():
    if len(podreczniki) == 0:
        print("\nNie ma żadnych podręczników do usunięcia.")
        return

    wyswietl_podreczniki()

    try:
        numer = int(input("\nPodaj numer podręcznika do usunięcia: "))

        if 1 <= numer <= len(podreczniki):
            usuniety = podreczniki.pop(numer - 1)
            print(
                f"\nUsunięto podręcznik: "
                f"{usuniety['tytul']}"
            )
        else:
            print("Nie ma podręcznika o takim numerze.")

    except ValueError:
        print("Podaj poprawny numer.")


def menu():
    while True:
        print("\n==============================")
        print("   KIERMASZ PODRĘCZNIKÓW")
        print("==============================")
        print("1. Dodaj podręcznik")
        print("2. Wyświetl podręczniki")
        print("3. Wyszukaj podręcznik")
        print("4. Usuń podręcznik")
        print("5. Zakończ program")
        print("==============================")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            dodaj_podrecznik()

        elif wybor == "2":
            wyswietl_podreczniki()

        elif wybor == "3":
            wyszukaj_podrecznik()

        elif wybor == "4":
            usun_podrecznik()

        elif wybor == "5":
            print("\nDziękuję za skorzystanie z kiermaszu!")
            break

        else:
            print("\nNieprawidłowa opcja. Wybierz 1-5.")


menu()
