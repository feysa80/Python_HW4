#Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
number = int(input('Введите число: '))
index = 2
dividers = []
while number > 1:
    if number % index == 0:
        dividers.append(index)
        number = number / index
    else: index += 1


print(dividers)
