# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input())
numbers = []
comp = 0
result = []
for i in range(n):
    a = input()
    numbers.append(a)
print(numbers)
for i in range(int(len(numbers)/2)):
    comp = int(numbers[i]) * int(numbers[-1 - i])
    result.append(comp)

if (len(numbers)%2 == 1):
    comp = int(numbers[int(n/2)]) * int(numbers[int(n/2)])
    result.append(comp)

print(result)
