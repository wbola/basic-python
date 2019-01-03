# Stwórz wykres funkcji f(x) = 3x + 1. Niech wykres będzie czerwoną przerywaną linią.

import matplotlib.pyplot as plt

y = [3*i+1 for i in range(0,10)]
plt.plot(y, 'r--')
plt.title('Wykres funkcji liniowej')
plt.show()