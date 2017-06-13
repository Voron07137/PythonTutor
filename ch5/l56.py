n = 100
E = {s for s in range(1, n + 1)}
A1 = {s for s in E if s % 5 == 2}
A2 = {s for s in E if s % 5 == 4}
A = A1 | A2
B = {s for s in E if s % 7 == 3}
C = {s for s in E if s % 3 == 1}
D = (A & B) - C
print("Приведённые ниже числа от 1 до", n)
print("1) при делении на 5 дают в остатке 2 или 4;")
print("2) при делении на 7 дают в остатке 3;")
print("3) при делении на 3 не дают в остатке 1;")
print(D)
