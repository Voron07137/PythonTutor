import copy

A = [[10, 20], [[30, 40], [50, 60]]]
B = copy.deepcopy(A)
print("Список A", A)
print("Список B", B)
print("Выполняются команды A[0][1] = 0 и A[1][1][1] = 0.")
A[0][1] = 0
A[1][1][1] = 0
print("Список A", A)
print("Список B", B)
