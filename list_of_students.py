# Stwórz w programie listę studentów. Każdy student powinien być
# krotką (imię, nazwisko, [ocena_z_algebry, ocena_z_analizy, ocena_z_wf]).
# Napisz program do wypisywania studentów o średniej powyżej 4.0.


studenci = [('Jan','Kowalski',[4,5,4]),('Jerzy','Nowak',[3,4,5]),('Andrzej','Waszak',[3,5,6]),('Marta','Kowalska',[2,4,6]),('Anna','Górska',[5,4,4])]
for i in studenci:
    srednia = sum(i[2])/len(i[2])
    if srednia>4:
        print(i[0],i[1])