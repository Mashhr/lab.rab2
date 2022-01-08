import re
print("Задание 5.1")
text="Предложение с точкой. Предложение с восклицательным знаком! Предложение с вопросительным знаком? Предложение с многоточием …"
a=re.split(r"(?<=[.!?…])", text)
print(a)
print("Задание 5.2")
print("Введите текст:")
text2=input()
b=re.sub(r"редиск\w+|Редиск\w+|нехорош\w+\s\человек\w","*давайте жить дружно*", text2)
print(b)
print("Задание 5.3")
c=0
print("Введите пароль")
d=input()
while c==0 :
    if c==0 :
        e=re.findall(r"[.?!]",d)
        f=re.findall(r"[a-zA-Zа-яА-ЯёЁ]",d)
        if len(d)<6 or len(e)<0 or len(f)<0 :
          print("Пароль не является надежным")
        else :
            print("Пароль надежный")
    c=1
print("Задание 5.4")
print("Введите адрес электронной почты")
adress=input()
j=r"^([a-z0-9_.-]+)@(([a-z0-9-]+\.)+[a-z]{2,6})$"
k=re.compile(j, re.I |re.S)
l=k.search(adress)
if not l:
   print("Электронный адрес не соответствует требованиям")
else:
   print(m.group(0), "Электронный адрес соответствует шаблону")
   print("Логин:", l.group(1), "Домен:", l.group(2))
print("Задание 5.5")
print("Введите строку с датой")
data=input()
data1 = re.sub(r'(\d{1,2}).(\d{1,2}).(\d{2,4})', r'\3-\2-\1', data)
data2 = re.findall(r'\d{2,4}.\d{1,2}.\d{1,2}', data1)
for i in data2:
  aa=[]
  aa.append(i)
  bb=aa[0].split("-")
  bb = [int(i) for i in bb]
  if 1 <= bb[1] <=12 and 1<= bb[2] <=31  :
     print("Верный формат даты:  ", bb[0], "-",bb[1],"-",bb[2])
  else:
    print("Неверный формат даты: ", bb[0], "-",bb[1],"-",bb[2])
   
