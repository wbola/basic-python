# Zapisz skrótowo:

# Lista kwadratów liczb naturalnych z przedziału [0,50]
print([x ** 2 for x in range(0,51)])

# sześciany liczb naturalnych z zakresu 20 do 30
print([x ** 3 for x in range(20,31)])

# wartości funkcji 3x-2 na liczbach całkowitych przedziale od -5 do 5
print([3*x - 2 for x in range(-5,6)])

# pary (x,y), gdzie x jest liczbą naturalną z zakresu 10-20, a y liczbą naturalną z zakresu 5-10
i=[x for x in range(10,21)]
j=[y for y in range(5,10)]
print([(x,y) for x in i for y in j])

# Lista par (x,y), gdzie x jest liczbą całkowitą z przedziału [4,7], a y jednym z napisów 'jabłko', 'gruszka' lub 'komputer'
a=[x for x in range(4,8)]
b=['jablko','gruszka','komputer']
print([(x,y) for x in a for y in b])