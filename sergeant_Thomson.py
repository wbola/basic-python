# Sierżant Thomson postanowił cenzurować listy, które otrzymują jego żołnierze. 
# Z każdego listu postanowił skreślić co trzecią linijkę, oraz dodatkowo skreślać te, 
# które zawierają słowo "kocham" (obojętnie, czy pisane wielką, czy małą literą). 
# Pomóż sierżantowi w tym zadaniu. Napisz program, który czyta list z jednego pliku, 
# a w innym pliku zapisuje jego ocenzurowaną wersję. 
# Ocenzurowane linie powinny być zastąpione ciągiem znaków '*****'.


with open('test.txt') as plik, open('wyslij.txt','w') as plik2:
        licznik = 0
        for linia in plik:
            licznik = licznik + 1
            dlugosc = len(linia) - 1
            if licznik % 3 == 0:
                plik2.write('***** \n')
            elif linia.count("kocham")>=1 or linia.count("Kocham")>=1:
                plik2.write('***** \n')
            else:
                plik2.write(linia)