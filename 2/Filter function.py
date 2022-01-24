#filter(func, iterable) – filter out items based on a test function
res = list(filter((lambda x: x >=0),[0,-1,3,-6]))
print(res)

r = list(filter((lambda x:x.find('W')>=0),['Hi','Hello','World']))
print(r) #World


people = [{'name':"Ann",'age':26},
{'name':"Kaio",'age':10},
{'name':"Kazumi",'age':30}]

#filter
p = filter(lambda x:x['age']>18,people)
