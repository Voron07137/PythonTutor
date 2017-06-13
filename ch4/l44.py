a = [10, 20, 30]
print("Список a:", a)
b = a
c = a[:]
d = a.copy()
print("Список b:", b)
print("Список c:", c)
print("Список d:", d)
print("Меняем значение элемента a[1]=0.")
a[1] = 0
print("Список a:", a)
print("Список b:", b)
print("Список c:", c)
print("Список d:", d)
