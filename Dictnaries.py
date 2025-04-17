dict7 = {101:'govindha',2:'Shiva'}

print(list(dict7.values()))
print(list(dict7.keys()))
print(list(dict7.items()))

print('key',dict7[101]) # indices are printing values only
print(dict7[2])

for key,value in dict7.items():
    if value !='govindha':
        print(f"{key}:{value}")


print(dict7)


dict1 = {'lord':'govindha','shiva':'mahadeva'}

print(dict1['shiva'])
print(type(dict1))

dict2 ={101:'govindha','108':'shiva',103:'Brhama'}

dict2[108]='somaya'
dict2[107]='Deva'
del dict2[108]
print(dict2)

for i in dict2:
    print(i)
    print(i,dict2[i])

new1 = {}
print(type(new1))

new1['venkateshwara']='seven'
new1['laddu']= 'appam'
print(new1)


dict5 = {}

for i in range(1,6):
    dict5[i]=i**2
print(dict5)


l1 = [(1,2),(3,4)]
l2 = [(5,6),(7,8)]
d1 = dict(zip(l1,l2)) # in zip function multiple aruguments in second list then it will asign whatever in first.
print(d1)

l3 = dict(((1,2),(3,4),(5,6)))
print('tuple',l3)


