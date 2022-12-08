# Вычислить число Пи c заданной точностью d
# Пример:- при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10

import math

d = float(input('Задайте точность, наример - d = 0.0001: '))
index = 1
while d < 1:
    d *= 10
    index *= 10
print(f'Результат: {int(math.pi*index)/index}')
