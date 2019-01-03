# Napisz program, który sprawdza, czy podany przez użytkownika rok jest przestępny. Rok jest
# przestępny jeśli jest podzielny przez 4, ale nie jest podzielny przez 100, właczając lata podzielne
# przez 400.

rok = int(input('Podaj rok: '))
if rok%4==0 and rok%100!=0 or rok%400==0:
	print("Rok jest przestępny")
else:
	print("Rok nie jest przestępny")