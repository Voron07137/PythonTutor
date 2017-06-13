s = [i * (10 - i) for i in range(11)]
print(s)
print("Удаляем элемент", s.pop(5))
print(s)
s.remove(21)
print(s)
del s[3]
print(s)
s[2:5] = []
print(s)
s[1:3] = [-1, -2, -3, -4, -5]
print(s)
