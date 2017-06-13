txt = "Мы изучаем " "Python"
print(txt)
print("Всего", len(txt), "букв")
print("Индекс\tБуква")
for i in range(len(txt)):
    print(str(i) + ":  \t" + txt[i])
print(txt[11:])
print(txt[::-1])
word = "Java"
txt = txt[:3] + "не" + txt[2:11] + word
print(txt)
