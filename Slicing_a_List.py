
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
