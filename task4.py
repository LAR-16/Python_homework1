# Задача 4 про Петю, Катю, Сережу и журавликов

number = int(input("Введите число: "))
while number % 6 != 0:
    number = int(input("Введите число: "))
petya=number//6
sergey=petya
kate=(sergey+petya)*2
print(f'''Петя сделал {petya} журавликов, 
Сережа сделал {sergey} журавликов, 
Катя сделала {kate} журавликов''')