# Napisz program, który przeczyta plik tekstowy linia po linii.
# Każda linia powinna być sprowadzona do małych liter, a ostatnie 5 znaków linii powinno być powtórzone.
# Wypisz zmienione linie.

with open('tekst.txt') as plik:
    for linia in plik:
        print((linia.rstrip().lower())+linia[-6:].rstrip().lower())