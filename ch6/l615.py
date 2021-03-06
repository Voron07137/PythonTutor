class ComplNum:
    def __init__(self, x=0, y=0):
        if type(x) == ComplNum:
            self.Re = x.Re
            self.Im = x.Im
        else:
            self.Re = x
            self.Im = y

    def show(self):
        print("Re =", self.Re)
        print("Im =", self.Im)


a = ComplNum(1, 2)
b = ComplNum(a)
print("Экземпляр a:")
a.show()
print("Экземпляр b:")
b.show()

print("Поля экземпляра a изменяются!")
a.Re = 10
a.Im = 20
print("Экземпляр a:")
a.show()
print("Экземпляр b:")
b.show()
