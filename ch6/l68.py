class MyClass:
    name = "Класс MyClass"

    def set(self, n):
        self.nickname = n

    def get(self):
        print("Значение поля:", self.nickname)

    def __init__(self, n):
        self.set(n)
        print("Создан экземпляр класса.")
        self.get()


green = MyClass("Зеленый")
print("Принадлежность:", green.name)
red = MyClass("Красный")
print("Принадлежность:", red.name)
green.name = "Здесь был Зеленый"
print("Спрашивает Красный:", red.name)
print("Спрашивает Зеленый:", green.name)
MyClass.name = "Здесь могла быть Ваша реклама!"
print("Спрашивает Красный:", red.name)
print("Спрашивает Зеленый:", green.name)
del green.name
print("Спрашивает Зеленый:", green.name)
