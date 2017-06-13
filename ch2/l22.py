res = eval(input("Введите что-нибудь: "))
resType = type(res)
if resType == int:
    print("Это целое число!")
if resType == float:
    print("Это действительное число!")
if resType != int and resType != float:
    print("Наверное, это текст!")
print("Работа завершена!")