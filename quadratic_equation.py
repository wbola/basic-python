# Napisz program do wyznaczania pierwiastków równania kwadratowego.

import math
a = float(input('Podaj wartość a: '))
b = float(input('Podaj wartość b: '))
c = float(input('Podaj wartość c: '))
delta = b*b - 4*a*c
if delta > 0:
    x1 = (-b - math.sqrt(delta))/(2*a)
    print(x1)
    x2 = (-b + math.sqrt(delta))/(2*a)
    print(x2)
elif delta == 0:
    x0 = -b/(2*a)
    print(x0)
else:
    print('Równanie kwadratowe nie posiada pierwiastków')