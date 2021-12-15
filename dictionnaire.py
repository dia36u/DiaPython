## DIA BABACAR IA SIMPLON 2021

#%%
# Pet Names

petNames={  'felix': 'cat', 
            'rex': 'dog', 
            'titi': 'bird',
        }
for name, kind in petNames.items():
    print('%s is a %s' %(name,kind))
# %%
# Polling Friends

questions={'gautier': 'i like it!',
           'rita': 'yes of course!',
           'bernard': 'not at all!',
        }
for name,answer in questions.items():
    print('Do you like chocolate %s ? - %s' % (name,answer))

# %%
# Pet Names 2
def show_dictionary(dictionary_name):
    print('\n this is my differents animals:\n')
    for name, kind in dictionary_name.items():
        print('%s is a %s' %(name,kind))

petNames={  'felix': 'cat', 
            'rex': 'dog', 
            'titi': 'bird',
        }
show_dictionary(petNames)
petNames['felix'] = 'egyptian cat'
show_dictionary(petNames)
petNames['dumbo'] = 'elephant'
show_dictionary(petNames)
del petNames['titi']
show_dictionary(petNames)

# %%
# Mountain Heights
mountain={
            'Everest':8848,
            'Machapuchare':6993,
            'San José':5856,
            'Mount Blackburn':4996,
            'Bishorn':4153,
        }
print('This is the 5 mountains I have choose to analyse:\n')
for name in mountain:
    print('%s' % name)
print('\nThis is the height of each mountain:\n')
for height in mountain.values():
    print('%i' % height)
print('\nLet\'s see the corresponding height for each mountain:\n')
for name,height in mountain.items():
    print('%s is %i meters tall' %(name,height))

# %%
# Montain Heights 2

mountain={
            'Everest':8848,
            'Machapuchare':6993,
            'San José':5856,
            'Mount Blackburn':4996,
            'Bishorn':4153,
        }
print('This is the 5 mountains I have choose to analyse:\n')
for name in mountain:
    print('%s' % name)
print('\nThis is the height of each mountain:\n')
for height in mountain.values():
    print('%i' % height)
print('\nLet\'s see the corresponding height for each mountain:\n')
for name,height in sorted(mountain.items()):
    print('%s is %i meters tall' %(name,height))
# %%
# Mountain Heights 3

mountain={
            'Everest':[8848, 8848* 3.28],
            'Machapuchare':[6993,6993* 3.28],
            'San José':[5856,5856* 3.28],
            'Mount Blackburn':[4996,4996* 3.28],
            'Bishorn':[4153,4153* 3.28],
        }
print('This is the 5 mountains I have choose to analyse:\n')
for name in mountain:
    print('%s' % name)

print('\nThis is the height in meters of each mountain:\n')
for height in mountain.values():
    print('%i' % height[0])

print('\nThis is the height in feets of each mountain:\n')
for height in mountain.values():
    print('%i' % height[1])
print('\nHere is all the infos about mountains:\n')
for name,height in mountain.items():
    print('%s is %i meters tall or %i feets.' % (name,height[0],height[1]))

# %%
# Mountain Heights 3 Bonus

def meter_to_feet(elevation):
    # feet = [meter*3.28 for meter in elevation]
    # return feet
    return [meter*3.28 for meter in elevation]


mountain={
            'Everest':8848,
            'Machapuchare':6993,
            'San José':5856,
            'Mount Blackburn':4996,
            'Bishorn':4153,
        }

feet=meter_to_feet(mountain.values())
#print(feet)


# for name in mountain:
#   mountain[name]=[mountain[name],feet.pop(0)]
for name,f in zip(mountain,feet):
    mountain[name]=[mountain[name],f]
print(mountain)


# %%
# Mountain Heights 4

mountains={
            'everest':{'elevation':8848, 'range':'himalayas'},
            'machapuchare':{'elevation':6993, 'range':'himalayas'},
            'san josé':{'elevation':5856, 'range':'andes'},
            'mount blackburn':{'elevation':4996, 'range':'wrangell mountains'},
            'bishorn':{'elevation':4153, 'range':'pennine alps'},
        }

print('This is the 5 mountains I have choose to analyse:\n')
for name in mountains:
    print('%s' % name.title())

print('\nThis is the height in meters of each mountain:\n')
for height in mountains.values():
    print('%i meters' % height['elevation'])

print('\nThis is the range of each mountain:\n')
for height in mountains.values():
    print('%s.' % height['range'].title())

print('\nHere is all the infos about mountains:\n')
for name,height in mountains.items():
    print('%s is an %i-meter tall in the %s range.' % (name.title(),height['elevation'],height['range'].title()))    

# %%
