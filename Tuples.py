#### Gymnast Scores

score=tuple(range(1,11))
print('The lowest possible score is %d, and the highest possible score is %d.'%(min(score),max(score)))
for number in score:
    for number in score[number-1:1]:
        print('A judge can give a gymnast %d point.'%(score[number-1]))
    print('A judge can give a gymnast %d points.'%(score[number-1]))

#### Revision with Tuples

print()
wallets=[0,10,500,30,1000]
print('The fattest wallet has $%d in it.'%max(wallets))
print('The skinniest wallet has $%d in it.'%min(wallets))
print('All together, these wallets have $%d in them.'%sum(wallets))

print()
Names=['jean','claude','richard','paul','antoine']
AwesomeGuys=['%s is awesome!'%name for name in Names]
for name in AwesomeGuys:  
    print(name.title())

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