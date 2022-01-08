import re
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


