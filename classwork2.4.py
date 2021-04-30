date1 = input('Задайте дату в формате "гггг-мм-дд чч:мм" ')
date = dict()
date1 = date1.replace('-', ' ')
date1 = date1.replace(':', ' ')
date1 = date1.split()
keys = ['year','month','day','hours','minutes']
for i in range(5):
    date[keys[i]] = date1[i]
print(date, type(date))