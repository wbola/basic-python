# Napisz program, który sprawdzi, czy użytkownik podał prawidłowo:

# kod pocztowy
import re
kod_pocztowy = input('podaj kod pocztowy: ')
dopasowanie = re.match(r'^[0-9]{2}\-[0-9]{3}$', kod_pocztowy)
if dopasowanie:
    print('OK')
else:
    print('Błąd')

# numer telefonu
import re
numer_telefonu = input('podaj numer telefonu: ')
dopasowanie = re.match(r'^\(\+[0-9]{2}\) [0-9]{9}$', numer_telefonu)
if dopasowanie:
    print('OK')
else:
    print('Błąd')

# adres e-mail
import re
adres_email = input('podaj adres email: ')
dopasowanie = re.match(r'^[a-z0-9A-Z]{1,}\@[a-z\.]{1,}$', adres_email)
if dopasowanie:
    print('OK')
else:
    print('Błąd')