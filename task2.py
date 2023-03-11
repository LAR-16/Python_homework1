# Задача 2
# Найдите сумму цифр трехзначного числа.

number = int(input("Введите трехзначное число: "))
while number > 999 or number < 100:
    number = int(input("Введите трехзначное число: "))

sum = 0
while number > 0:
    sum += number % 10
    number = number//10
print(sum)
