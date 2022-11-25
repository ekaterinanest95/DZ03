# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = int(input())
numbers = []

for i in range(n):
    a = float(input())
    f = a - int(a)
    numbers.append(round(f, 2))
    if f == 0.0:
        numbers.remove(0.0)

print(numbers)

max_number = float(numbers[0])
min_number = float(numbers[1])
result = 0

for i in range(len(numbers)):
    if(numbers[i] > max_number):
        max_number = numbers[i]
    else:
        i +=1
print(max_number)

for i in range(len(numbers)):
    if(numbers[i] < min_number):
        min_number = numbers[i]
    else:
        i +=1
print(min_number)

result = max_number - min_number
print(result)




