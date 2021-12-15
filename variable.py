# DIA BABACAR IA SIMPLON 2021
#%%
# Hello World - variable
message = "Hello people of Simplon!"
print(message)

# One Variable, Two Messages:

message = "Hello people of Simplon.co!"
print(message)

#%%
#Someone Said

quote ="Lao-Tseu à dit: 'Si tu donnes un poisson à un homme, il mangera un jour. Si tu lui apprends à pêcher, il mangera toujours.'"
print(quote)

# First Name Cases

prenom = "babacar"
print(prenom)
print(prenom.title())
print(prenom.upper())

# Full Name

nom = "dia"
print(prenom + ' ' + nom)

# About This Person

prenomPerson = "lao"
nomPerson = "tseu"
citation = prenomPerson.title() + '-' + nomPerson.title() + ' à dit: \'Si tu donnes un poisson à un homme, il mangera un jour. Si tu lui apprends à pêcher, il mangera toujours.\''
print(citation)

# Name Strip

prenomWhitespace = " babacar "
print(prenomWhitespace)
print(prenomWhitespace.lstrip())
print(prenomWhitespace.rstrip())
print(prenomWhitespace.strip())
#%%
#Arithmetic

num1 = 3
num2 = 6
num3 = 2
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1**num2)

# Order of Operations

print (num1+num2*num3)
print ((num1+num2)*num3)


# Long Decimals

print(0.1+0.7)

# Python 2 or Python 3?

print(4/2)
print(3/2)
#%%
# Challenges Neat Arithmetic

a=6*3
b=15-3
c=8/2
d=10+2
e=10**2

print('The result of the calculation 6x3 is %i' % a)
print('The result of the calculation 15-3 is %i' % b)
print('The result of the calculation 8/2 is %i' % c)
print('The result of the calculation 10+2 is %i' % d)
print('The result of the calculation 10^2 is %i' % e)

# %%
# Neat Order of Operations


print (3+6*2)
print ((3+6)*2)

print ('6x2=%i|3+%i=%i' % (6*2,6*2,6*2+3))
print ('3+6=%i|%ix2=%i| l\'addition devient prioritaire' % (3+6,3+6,(3+6)*2))
# %%


