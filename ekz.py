
#Пройти циклом по словарю и найти максимальное значение

import random 
shop = {"молочное":1, "сладкое":2,"овощи":3, "фрукты":4,"мясо":5}
max_shop = max(shop.values())
print(max_shop)



#реализовать кортеж с рандомными числами и вывести все нечетные числа
d = [1, 5, 8, 2, 3, 4, 6, 7, 9, 23]

for i in range(len(d)):
    if (i.__index__() % 2 == 0) and i.__index__() != 0:
        print(d[i])
    
#Нужно было написать рандомный список, который бы выводил сумму всех элементов
dict= {'a': 1, 'b': 3, 'c': 2, 'd': 0, 'e': 5}
max_val = max(dict.values())
print(max_val)
final_dict = {k:v for k, v in dict.items() if v == max_val}
print(final_dict)

from functools import reduce
list = [1,2,3,4]
s=reduce(lambda x,y:x+y,list)
print(s)
print(sum(list))

#Уникальные значения в списке

#a=[1,2,2,5,5,7,8,9,10,8,9,9]
#b=list(set(a))

#print (len(a)-len(b))
#функция



def add(x,y):

    test = tuple([random.randint(0,y)
    for i in range(x)
    ])
    print(test)
add(10,10)
#создать список из букв и цифр и возвращает только цифры
list = [1,2,3,'a','b']
for i in list:
    if type(i) is int :
        print(i)

l = [1,2,3,'a','b']


def sorted(x,y):
    for i in l:
        if type(i) is not int:
            y.append(i)
    print(y)
l2=[]
sorted(l,l2)
#ретерн имеет смысл когда значения не передаются

