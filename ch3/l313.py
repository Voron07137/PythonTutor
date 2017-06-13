x = 100


def tes_vars():
    global x, y
    print("В теле функции x =", x)
    y = 200
    print("В теле функции y =", y)
    x = 300


tes_vars()
print("Вне функции x =", x)
print("Вне функции y =", y)
