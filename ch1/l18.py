a = float(input("Введите первое число "))
b = float(input("Введите второе число "))
value_1 = "Первое число больше второго"
value_2 = "Второе число не меньше первого"
res = value_1 if a > b else value_2
print(res)