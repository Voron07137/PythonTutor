class MyClass:
    pass


A = MyClass()
B = MyClass()
A.first = "Экземпляр A"
B.second = "Экземпляр B"
MyClass.total = "Класс MyClass"

print(A.total, "->", A.first)
try:
    print(A.second)
except AttributeError:
    print("Такого поля у экземпляра A нет!")

print(B.total, "->", B.second)
try:
    print(B.first)
except AttributeError:
    print("Такого поля у экземпляра B нет!")

del MyClass.total
try:
    print(A.total)
except AttributeError:
    print("Такого поля нет!")
try:
    print(B.total)
except AttributeError:
    print("Такого поля нет!")

del A.first
try:
    print(A.first)
except AttributeError:
    print("Такого поля у экземпляра A нет!")
