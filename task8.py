# Задача 8 про шоколадку

n = int(input("Введите число долек: "))
m = int(input("Введите второе число долек: "))
k = int(input("Сколько хотите получить долек?: "))
while k >= n*m:
    k = int(input("Введите другое количество долек: "))
if k % n == 0 or k % m == 0:
    print("Да, шоколадку можно так поломать")
else:
    print("Нет, шоколадку нельзя так поломать")
