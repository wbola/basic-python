# Napisz program do obliczania Body Mass Index (BMI). Użytkownik podaje swoją wagę i wzrost,
# program oblicza BMI i wypisuje komunikat o ewentualnej nadwadze (> 25) lub otyłości (> 30).

waga = float(input('Podaj swoją wagę: '))
wzrost = float(input('Podaj swój wzrost w metrach: '))
BMI =  waga/(wzrost ** 2)
print('BMI: ', BMI)
if BMI > 25 and BMI <= 30:
    print('nadwaga')
elif BMI > 30:
    print('otyłość')