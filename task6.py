# Задача 6 про счастливый билетик

number = int(input("Введите номер билета: "))
while number > 999999 or number < 100000:
    number = int(input("Введите другой номер: "))
sum1 = 0
while number >1000:
    sum1 += number % 10
    number = number//10

sum2=0
while number >0:
    sum2 += number % 10
    number = number//10
if sum1==sum2:
    print("Билет счастливый, вам повезло!!")
else:
    print("Билет не счастливый((( Не расстраивайся, повезет в другой раз")