numeric = str(input()) #Ввод слова
x = len(numeric) #Сохраняем длину слова
i = 0
x = x - 1
k = 0
#Проверка на полиндром
while x - i >= i:
    if numeric[x - i] == numeric[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
  print("no")
else:
  print("yes")
#Savoskina
