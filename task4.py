# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100)* многочлена и записать в файл многочлен степени k.
import random

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0
k = int(input("Задайте степень многочлена: "))
mn_count = random.randint(1, k) #количество членов в многочлене
result = ''
mn_list = [random.randint(1, 100)]
k_safe = k
if mn_list[0] == 1:
    if k == 1:
        result += f'x'
    else:
        result += f'x^{k}'

elif k == 1:
    result += f'{mn_list[0]}*x'
else:
    result += f'{mn_list[0]}*x^{k}'

for i in range(1, mn_count):
    mn_list.append(random.randint(0, 100))

k -= 1
for i in range(1, len(mn_list)-1):
    if mn_list[i] == 1:
        result += f' + x^{k}'
    elif mn_list[i] > 1:
        result += f' + {mn_list[i]}*x^{k}'
    k -= 1
if mn_list[-1] == 1:
    result += f' + x = 0'
elif mn_list[-1] > 1 and len(mn_list)>1:
    result += f' + {mn_list[-1]}*x = 0'
else:
    result += ' = 0'

with open('task4.txt', 'w') as data:
    data.write(f'Для степени {k_safe} со случайными коэффициентами: {mn_list}\n')
    data.write(f'Многочлен: {result}\n')


