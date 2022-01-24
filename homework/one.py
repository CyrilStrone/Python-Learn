print("Ваш пол(0-м, 1-ж): ")
sex = int(input())
if sex ==0:
    sex = 0.8
else:
    sex = 0.5

print("Расстояние(метры): ")
distance = int(input())
print("Время ходьбы(минуты): ")
time = int(input())

steps = distance/sex
print(steps," шагов ты прошел")
average = (distance/1000)/(time/60)
print(average," км/ч")

if average<2:
    print('Low')
elif 2<=average<=3:
    print('побольше ходи!!!')
elif 4<=average<=5:
    print('продолжай в том же духе!')
elif 6<=average<=10:
    print('а ты герой!')
else:
    print('High')


