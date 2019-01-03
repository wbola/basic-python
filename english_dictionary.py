# Stwórz słownik dziesięciu słówek angielskich, indeksowany odpowiadającymi im słówkami polskimi.
# Napisz program, który poprosi użytkownika o podanie słowa polskiego i wypisze tłumaczenie ze słownika.

slownik = {'tak' : 'yes', 'nie' : 'no', 'pies' : 'dog', 'kot' : 'cat', 'proszę' : 'please', 'dodawać' : 'add', 'znowu' : 'again', 'i' : 'and', 'lub' : 'or', 'średnia' : 'average'}
a=input('Podaj słówko polskie: ')
print(slownik[a])