# DIA BABACAR IA SIMPLON 2021
#%%
#######################################################################
#### First List

langages = ['python','c','java']
print(langages[0].title())
print(langages[1].title())
print(langages[2].title())
#### First Neat List

print('the best langage is '+langages[0].title())
print('the langage I\'m the worst at is '+langages[1].title())
print('the langage I want to be better at is '+langages[-1].title())

#### Your First List

fruits = ['banane','pomme','fraise']
print("my favorite fruit is "+ fruits[0])

# %%
#######################################################################
#### First List - Loop

langages = ['python','c','java']
for langage in langages: 
    print(langage.title())

#### First Neat List - Loop

for langage in langages: 
    print('the best langage is '+langage)

#### Your First List - Loop

fruits = ['banane','pomme','fraise']
for fruit in fruits:
    print("my favorite fruit is "+ fruit)
#%%
#######################################################################
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

#%%
#######################################################################
#### Famous People
famousPeople=['Michael Jackson', "Dwayne Johnson", "Bill Gates", "Omar Sy"]
print(famousPeople)
famousPeople.pop()
famousPeople.pop(0)
del famousPeople[0]
famousPeople.remove('Bill Gates')
print("there are no famous people left in the list")
print(famousPeople)
#%%
#######################################################################
#### Alphabet Slices
letters=['a','b','c','d','e','f','g','h','i','j']
batch1=letters[:3]
print(batch1)
batch1=letters[3:6]
print(batch1)
batch1=letters[5:]
print(batch1)

#### Protected List

famousPeople=['Michael Jackson', "Dwayne Johnson","Omar Sy"]
copyfamousPeople=famousPeople[:]
copyfamousPeople.append('Bill Gates')
copyfamousPeople.append('Madona')
print('\nthis is the original list:\n')
for name in famousPeople:
    print(name)
print('\nthis is the copied list:\n')
for name in copyfamousPeople:
    print(name)
#%%
#######################################################################
#### First Twenty
numbers = list(range(1,21))
print(numbers)

#### Larger Sets
# numbers = list(range(1,10000001))
# print(numbers)

# #### Five Wallets
wallets=[0,10,500,30,1000]
print('The fattest wallet has $'+str(max(wallets))+' in it.')
print('The skinniest wallet has $'+str(min(wallets))+' in it.')
print('All together, these wallets have $'+str(sum(wallets))+' in them.')

print()

Working_List=[]
print(Working_List)
Working_List.append('programmer')
Working_List.append('architect')
Working_List.append('truck driver')
Working_List.append('dentist')
Working_List.append('hunter')
Working_List.append('dj')
print(Working_List)
print('first career %s'%Working_List[0])
print('last career %s'%Working_List[-1])
#%%
#### Multiples of Ten
multipleOfTen=[FirstTenNumber*10 for FirstTenNumber in range(1,11)]
print(multipleOfTen)

# #### Cubes
FirstTenSquares=[number**3 for number in range(1,11)]
print(FirstTenSquares)

# #### Awesomeness
Names=['jean','claude','richard','paul','antoine']
AwesomeGuys=[name+' is awesome!' for name in Names]
for name in AwesomeGuys:  
    print(name.title())

# #### Working Backwards

plus_thirteen=[]
for number in range(1,11):
    plus_thirteen.append(number+13)
print(plus_thirteen)
#%%
#######################################################################
#### Listing a Sentence
bonjour='Hello World!'
for letter in bonjour:
    print(letter)

# #### Sentence List
print(list(bonjour))

# #### Sentence Slices
firstFive=(bonjour[:5])
MiddleFive=(bonjour[2:7])
LastFive=(bonjour[-5:])
print(firstFive,MiddleFive,LastFive)

# #### Finding Python

sentence='Hello people of Python, I hate snake but I love Python!'
print('Python' in sentence)
print(sentence.find('Python'))
print(sentence.rfind('Python'))
print(sentence.count('Python'))
splitSentence=sentence.split(' ')
print(splitSentence)
for word in splitSentence:
    print(word)
print(sentence.replace('Python', 'Ruby'))
#%%
#######################################################################
#Counting DNA Nucleotides
sample='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
a=0
c=0
g=0
t=0
for letter in sample:
    if letter=='A':
        a=a+1
    elif letter=='C':
        c=c+1
    elif letter=='G':
        g=g+1
    elif letter=='T':
        t=t+1
print('A=%s|C=%s|G=%s|T=%s' % (a,c,g,t))

# %%
#######################################################################
# Transcribing DNA into RNA
sample='GATGGAACTTGACTACGTAAATT'
print(sample.replace('T','U'))
# %%
