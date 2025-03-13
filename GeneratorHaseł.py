import random
import string

haslo = []
pozostale_znaki = -1

def funkcja_znakow(znaki):
    global pozostale_znaki
    if znaki < 0 or znaki > pozostale_znaki:
        print("Podaj ilość z przedziału 0 -", pozostale_znaki)
        return False
    else:
        pozostale_znaki -= znaki
        print(f"Pozostało {pozostale_znaki} znaków")
        return True

while True:
    try:
        dlugosc_hasla = int(input("Podaj jaką chcesz długość hasła (minimum 5 znaków): "))
        if dlugosc_hasla < 5:
            print("Za mało znaków, podaj większą długość.")
            continue
        else:
            pozostale_znaki = dlugosc_hasla
            break
    except ValueError:
        print("Podaj prawidłową liczbę.")
        continue

while True:
    try:
        male_litery = int(input("Ile małych liter ma mieć hasło? "))
        if funkcja_znakow(male_litery):
            break
    except ValueError:
        print("Podaj prawidłową liczbę.")
        continue

while True:
    try:
        duze_litery = int(input("Ile dużych liter ma mieć hasło? "))
        if funkcja_znakow(duze_litery):
            break
    except ValueError:
        print("Podaj prawidłową liczbę.")
        continue

while True:
    try:
        znaki_specjalne = int(input("Ile znaków specjalnych ma mieć hasło? "))
        if funkcja_znakow(znaki_specjalne):
            break
    except ValueError:
        print("Podaj prawidłową liczbę.")
        continue

cyfry = pozostale_znaki
print("Cyfr użyje ",cyfry)

print(cyfry)
print()
print("Długość hasła = ",dlugosc_hasla)
print("Ilość małych liter = ",male_litery)
print("Ilość dużych liter = ",duze_litery)
print("Ilość znaków specjalnych = ",znaki_specjalne)
print("Ilość cyfr = ",cyfry)

for _ in range(dlugosc_hasla):
    if male_litery > 0:
        haslo.append(random.choice(string.ascii_lowercase))
        male_litery -= 1
    if duze_litery > 0:
        haslo.append(random.choice(string.ascii_uppercase))
        duze_litery -= 1
    if znaki_specjalne > 0:
        haslo.append(random.choice(string.punctuation))
        znaki_specjalne -= 1
    if cyfry > 0:
        haslo.append(random.choice(string.digits))
        cyfry -= 1

random.shuffle(haslo)
print(haslo)
haslo = "".join(haslo)

print("Twoje hasło: ",haslo)