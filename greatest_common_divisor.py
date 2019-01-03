# Napisać program do wyznaczania największego wspólnego dzielnika algorytmem Euklidesa.


a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))
r = a%b
while r != 0:
    a = b
    b = r
    r = a%b
print('NWD =', b)