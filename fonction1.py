# -*- coding: utf-8 -*-
# """
# Created on Tue Dec 14 15:02:27 2021

# @author: diaba
# """



#%%
## Greater

def congrats(name):
    print('congratulations %s! \n Your are awesome %s ! \n Keep it up %s!\n' %(name.title(),name.title(),name.title()))

names=['babacar','thomas','agathe']

for name in names:
    congrats(name)
#%%
## Full Names

def full_name(firstname,lastname):
    print('Hello, %s %s.' %(firstname.title(),lastname.upper()))

names=['babacar','thomas','agathe']
lastnames=['dia','edison','oderi']

full_name(names[0],lastnames[0])
full_name(names[1],lastnames[1])
full_name(names[2],lastnames[2])
#%%
## Addition Calculator

def addition(num1,num2):
    print('%i + %i = %i' %(num1,num2,num1+num2))

addition(2,3)
addition(10,40)
addition(20,1)

#%%
## Return Calculator

def returnCalculator(num1,num2):
    return num1+num2

num1=[2,10,20]
num2=[3,40,1]

print('%i + %i = %i' %(num1[0],num2[0],returnCalculator(num1[0],num2[0])))
print('%i + %i = %i' %(num1[1],num2[1],returnCalculator(num1[1],num2[1])))
print('%i + %i = %i' %(num1[2],num2[2],returnCalculator(num1[2],num2[2])))

# %%
