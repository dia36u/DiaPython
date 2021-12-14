## DIA BABACAR IA SIMPLON 2021

#%%
## Games

games=['football','video games','pokemon go']

def fav_games(game='chess'):
    print('I like playing %s' % game)

fav_games(games[0])
fav_games(games[2])
fav_games()

#%%
# Favorite Movie

movies=['titanic','inception','fast & furious']

def fav_movie(movie='the princess bride'):
    print('My favorite movie is %s' % movie.title())

fav_movie()
fav_movie(movies[1])
fav_movie(movies[2])

#%%
## Favorite Colors

def fav_color(name,color):
    print('%s favorite color is %s' % (name.title(),color))

names=['babacar','thomas','agathe']
colors=['blue','red','yellow']

fav_color(names[0],colors[0])
fav_color(names[1],colors[1])
fav_color(names[2],colors[2])

#%%
## Phones

def phone(brand,model):
    print('%s %s' % (brand.title(),model.title()))

brands=['iphone','samsung','xiaomi']
models=['4S','galaxy note 10','redmi note']

phone(brands[0],models[0])
phone(brands[1],models[1])
phone(brands[2],models[2])