people = [{'name':"Ann",'age':26},
{'name':"Kaio",'age':10},
{'name':"Kazumi",'age':30}]

p = map(lambda x:print(x['name']+"is"+str(x['age'])),people)
print(*p)