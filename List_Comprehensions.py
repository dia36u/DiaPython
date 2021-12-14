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
