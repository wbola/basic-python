# Napisz program, który zliczy linie, słowa i znaki w pliku tekstowym. 
# Słowem nazywamy ciąg znaków oddzielony białymi znakami.


with open('tekst.txt') as plik:
    linie = 0
    slowa = 0
    znaki = 0
    for linia in plik:
        znaki = znaki + len(linia)
        slowa = slowa+ len(linia.split())
        linie += 1

print ('Linie: ', linie)
print ('Slowa: ', slowa)
print ('Znaki: ', znaki)