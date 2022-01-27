import random
from random import randint
import numpy as np
shop = ["молочное", "сладкое","овощи", "фрукты","мясо"]
dairy = ["кефир", "йогурт","варенец", "простокваша","творог"]
sweet = ["сахар", "мед","варенье ", "шоколад","конфеты"]
vegetables = ["картофель", "репа","брюква", "редька","редис"]
fruit = ["яблоки", "груши","слива", "айва","ирга"]
meat = ["говядина", "баранина","свинина", "конина","козлятина"]
numfour = 0   
onof = 0
columns = 0
victory =99999
usershopnum = 1
allshop = []
usershop = []

        
def magazineone(x):   
     for i, item in enumerate(x):
                print(i + 1, item)

def magazinetwo(usershop,numfour,usershopnum,n,columns):
    numusertwo = int(input()) 
    for x in n:
       
        numfour = numfour + 1
        if numfour == numusertwo:
            numusertwo = numusertwo -1
            u = n[numusertwo]
            for i in range(usershopnum):
                if i == (usershopnum-1):
                    usershop.append([u])
                    usershopnum=usershopnum +1
    
def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count



while onof < 4:
    
    if onof == 0:
        print("Категории: \n1)молочное \n2)сладкое \n3)овощи \n4)фрукты \n5)мясо ")
        choise = int(input())
        onof =1

        if choise == 1:
            magazineone(dairy)
            magazinetwo(usershop,numfour,usershopnum,dairy,columns)
            columns = columns +1
            
        elif choise == 2:
            magazineone(sweet)
            magazinetwo(usershop,numfour,usershopnum,sweet,columns)
            columns = columns +1
        elif choise == 3:
            magazineone(vegetables)
            magazinetwo(usershop,numfour,usershopnum,vegetables,columns)
            columns = columns +1
        elif choise == 4:
            magazineone(fruit)
            magazinetwo(usershop,numfour,usershopnum,fruit,columns)
            columns = columns +1
        elif choise == 5:
            magazineone(meat)
            magazinetwo(usershop,numfour,usershopnum,meat,columns)
            columns = columns +1
        
    elif onof == 1:
        print(usershop," Это ваш список покупок") 
        print("1)Добавить\n\n2)Рассчитать пользу")
        choisetwo = int(input())
        if choisetwo==1:
            onof = 0
        elif choisetwo==3:
            onof = 3
        else:
            onof = 2
    elif onof == 2:
        onof = 4
    else:
        print("Плохой выбор")


for i in range(len(usershop)): 
    for j in range(len(usershop)):
        
        if i == 0:
            kal = randint(50, 500)
            fat = randint(50, 500)
            carbohydrates = randint(50, 500)
            protein = randint(50, 500)
            usershop[j].append(kal)
            usershop[j].append(fat)
            usershop[j].append(carbohydrates)
            usershop[j].append(protein)
                
print("Продукт ккал жиры углеводы протеин")
for i in range(len(usershop)): 
    print(usershop[i])
    print("\n")

for i in range(len(usershop)): 
    for j in range(len(usershop)):
        if j == 2:
            nonevictory = usershop[i][j]
            
            if nonevictory <=victory:
                
                victory = nonevictory
        if j == 1:
            
            nonevictory = usershop[i][j+1]
            
            if nonevictory <=victory:
                
                victory = nonevictory

for i in range(len(usershop)): 
    for j in range(len(usershop)):
        nonevictory = usershop[i][j+1]
        if nonevictory == victory:
            print("Продукт ккал жиры углеводы протеин")
            print("Меньше всего углеоводов:")
            print(usershop[i][0], end=" ")    
            print(usershop[i][1], end=" ")
            print(usershop[i][2], end=" ")  
            print(usershop[i][3], end=" ")
            print(usershop[i][4], end=" ")     
            



            
            
        
        
       

                                
                
a = 6 
b = 5
r = 0
        
for i in range(a):
    allshop.append([])
    for j in range(b):
        if i == 0:
            r = shop[j]
            allshop[i].append(r)
        elif i == 1:
            r = dairy[j]
            allshop[i].append(r)
        elif i == 2:
            r = sweet[j]
            allshop[i].append(r)
        elif i == 3:
            r = vegetables[j]
            allshop[i].append(r)
        elif i == 4:
            r = fruit[j]
            allshop[i].append(r)
        else:
            r = meat[j]
            allshop[i].append(r)

    
        
        



#привет меня зовут настюша у меня есть кот барсик ему 1000 лет

#500 лайков и 158 репостов