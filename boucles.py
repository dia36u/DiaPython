## DIA BABACAR IA SIMPLON 2021

#%%
## Growing Strength

strength = 5
print('the player strength is %i' % strength)
while strength < 10:
   print('the player current strength is %i' % strength)
   print('Wow! the player strength increase!')
   strength += 1
print('the player strength is to high for this place! Let\'s move!')

#%%
# Game Preferences

games=['chess','football','mölky','badminton']
print('i like %s' % games)
new_game=input('And you, what is your favorite game? : ')
games.append(new_game)
print('We like %s' % games)
# %%
## Many games

games=['chess','football','mölky','badminton']
print('i like %s' % games)
new_game =''
while new_game != 'quit':
    new_game=input('Add a game you like or press "quit : ')
    if new_game != 'quit':
        games.append(new_game)
print('We like %s' % games)
# %%

## Marveling at Infinity
clock=1
while clock !=0:
    print('time is running!')
    
# %%
