#### Working List
from abc import abstractproperty


workfields=['programmer','truck driver','dentist','hunter']
print(workfields.index('dentist'))
print('hunter' in workfields)
workfields.append('DJ')
workfields.insert(2,'architect')
for workfield in workfields:
    print(workfield)

#### Starting From Empty
Working_List=[]
print(Working_List)
Working_List.append('programmer')
Working_List.append('architect')
Working_List.append('truck driver')
Working_List.append('dentist')
Working_List.append('hunter')
Working_List.append('dj')
print(Working_List)
print('first career '+Working_List[0])
print('last career '+Working_List[-1])

#### Ordered Working List

print('\noriginal order:')
for work in Working_List:
    print(work)

print('\nalphabetical order:')
for work in sorted(Working_List):
    print(work)

print('\noriginal order:')
for work in Working_List:
    print(work)   

print('\nreverse alphabetical order:')
for work in sorted(Working_List, reverse=True):
    print(work)

print('\noriginal order:')
for work in Working_List:
    print(work)

print('\nreverse order:')
Working_List.reverse()
for work in Working_List:
    print(work)

print('\noriginal order:')
Working_List.reverse()
for work in Working_List:
    print(work)
      
print('\nalphabetical order:')
Working_List.sort()
for work in Working_List:
    print(work)  

print('\nreverse alphabetical order:')
Working_List.sort(reverse=True)
for work in Working_List:
    print(work)  

#### Ordered Numbers
numbers=[0,5,1,8,3]

print('\noriginal order:')
for number in numbers:
    print(number)

print('\nincreasing order:')
for number in sorted(numbers):
    print(number)

print('\noriginal order:')
for number in numbers:
    print(number)

print('\ndecreasing order:')
for number in sorted(numbers, reverse=True):
    print(number)

print('\noriginal order:')
for number in numbers:
    print(number)

print('\nreverse order:')
numbers.reverse()
for number in numbers:
    print(number)

print('\noriginal order:')
numbers.reverse()
for number in numbers:
    print(number)

print('\nincreasing order:')
numbers.sort()
for number in numbers:
    print(number)

print('\ndecreasing order:')
numbers.sort(reverse=True)
for number in numbers:
    print(number)

#### List Lengths

print("La liste numbers contient "+str(len(numbers))+" éléments")
print("La liste Working_List contient "+ str(len(Working_List))+" éléments")


