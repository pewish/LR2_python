d={}
i = 0
while i<5:
   value=int(input("Введите первое число: "))
   value2=int(input("Введите второе число: "))
   c = [value,value2]
   key=value+value2
   if key in d.keys(): 
      d[key] = c
      print("Такое ключ уже есть в списке:",*d.keys())
   else:
      d[key] = c
      print("Добавили новое значение")
   i=i+1
