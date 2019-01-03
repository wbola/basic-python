# Stwórz tabliczkę mnożenia 100x100 w formacie CSV. Otwórz ją w Excelu.

			
with open('tabliczka.csv', 'w') as tabliczka:
    for i in range(101):
        if i == 0:
            tabliczka.write(';')
        else:
            tabliczka.write(str(i) + ';')
    for i in range(101)[1:]:
        tabliczka.write("\n" + str(i) + ";")
        for n in range(101)[1:]:
            tabliczka.write(str(i*n) + ';')			