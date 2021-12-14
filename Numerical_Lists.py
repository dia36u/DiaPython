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