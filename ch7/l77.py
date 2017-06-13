class Alpha:
    "Класс Alpha и внутренний класс Bravo"

    def hello():
        pass

    class Bravo:
        pass


class Charlie(Alpha):
    pass


class Delta(Charlie):
    "Класс Delta наследует класс Charlie"
    pass


obj = Alpha()
print("Поле __class__")
print("Экземпляр obj:", obj.__class__)
print("Класс Alpha:", Alpha.__class__)
print("Класс Alpha.Bravo:", Alpha.Bravo.__class__)
print("Класс Charlie:", Charlie.__class__)

print("\nПоля __bases__ и __mro__")
print("Класс Delta, поле __bases__:", Delta.__bases__)
print("Класс Delta, поле __mro__:", Delta.__mro__)
print("Класс Alpha, поле __bases__:", Alpha.__bases__)
print("Класс Alpha, поле __mro__:", Alpha.__mro__)

print("\nПолe __doc__")
print("Описание класса Alpha:", Alpha.__doc__)
print("Описание класса Delta:", Delta.__doc__)

print("\nПолe __module__")
print("Модуль класса Alpha:", Alpha.__module__)

print("\nПолe __dict__")
print("Атрибуты класса Alpha:", Alpha.__dict__)
print("Атрибуты класса Alpha.Bravo:", Alpha.Bravo.__dict__)
print("Атрибуты класса Delta:", Delta.__dict__)

print("\nПоля __name__ и __qualname__")
print("Класс Alpha, поле __name__", Alpha.__name__)
print("Класс Alpha, поле __qualname__", Alpha.__qualname__)
print("Класс Alpha.Bravo, поле __name__", Alpha.Bravo.__name__)
print("Класс Alpha.Bravo, поле __qualname__", Alpha.Bravo.__qualname__)
print("Класс Delta, поле __name__", Delta.__name__)
print("Класс Delta, поле __qualname__", Delta.__qualname__)
