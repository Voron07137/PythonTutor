err_one = ZeroDivisionError("Ошибка деления на ноль!")
print("Сейчас \"возникнет\" ошибка.")
print("Первая:")
print(err_one)

try:
    raise err_one
except ZeroDivisionError as err_two:
    print("Вторая:")
    print(err_two)
    try:
        raise err_two
    except ZeroDivisionError as err_three:
        print("Третья:")
        print(err_three)
        try:
            a = 1 / 0
        except ZeroDivisionError as err_four:
            print("Четвертая:")
            print(err_four)
print("Больше никаких ошибок.")
