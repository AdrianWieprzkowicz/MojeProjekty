wybor = 0

zadania = []

def pokaz_zadania():
    for indeks, zadanie in enumerate(zadania):
        print(indeks+1, zadanie)

def dodanie_zadania():
    dodaje = input("Wpisz zadanie które chcesz dodać: ")
    zadania.append(dodaje)

def usuwanie_zadania():
    print("Zadania które można usunąć:")
    pokaz_zadania()
    try:
        usuwam = int(input("Podaj numer zadania: "))
        if 1 <= usuwam <= len(zadania):
            del zadania[usuwam - 1]
            print("Zadanie zostało usunięte")
        else:
            print("Podano niepoprawną wartość która nie jest numerem zadania")
    except ValueError:
        print("Podano niepoprawną wartość która nie jest numerem zadania")


def zapis_zadania():
    with open("MenadzerZadań.txt", "w") as zapis:
        for zadanie in zadania:
            zapis.write(zadanie + "\n")

def odczyt_zadania():
    try:
        with open("MenadzerZadań.txt") as plik:
            for linia in plik.readlines():
                zadania.append(linia.strip())
    except FileNotFoundError:
        return

odczyt_zadania()
while wybor != 5:
    print("(1) Pokaż zadania")
    print("(2) Dodaj zadanie")
    print("(3) Usuń zadanie")
    print("(4) Zapisz zmiany w pliku")
    print("(5) Wyjdź")

    try:
        wybor = int(input("Wybierz czynność(1-5): "))
        if wybor == 1:
            pokaz_zadania()
            print()
        elif wybor == 2:
            dodanie_zadania()
            print()
        elif wybor == 3:
            usuwanie_zadania()
            print()
        elif wybor == 4:
            zapis_zadania()
        elif wybor == 5:
            print("Dziękujemy za korzystanie z programu!")
        else:
            print("Wybrana wartość nie jest liczbą z przedziału (1-5)")
    except:
        print("Wybrana wartość nie jest liczbą z przedziału (1-5)")