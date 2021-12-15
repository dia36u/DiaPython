# -*- coding: utf-8 -*-

# Created on Tue Dec 14 13:34:07 2021

# @author: diaba

#%%
#### True and False

print(1 == 1)
print(3 == 3.0)
print(1+3 <= 5)
print(5 >= 5.0)
print(1 >= 0)

print(52-2>=51)
print('a' == 'A')
print('007' == 'OO7')
print(0>=0.5)
print(12<11)
#%%
##Tree is a Crowd
def crowd_test(size):
    if len(size) > 3:
      print('There is a lot of people here!') 

names=['jacques','henry','david','paul']
crowd_test(names)
del names[-1]
del names[-1]
crowd_test(names)
# %%
##Tree is a Crowd - Part 2

def crowd_test(size):
    if len(size) > 3:
        print('There is a lot of people here!')
    else:
        print('there is not a lot of people here!')
names=['jacques','henry','david','paul']
crowd_test(names)
del names[-1]
del names[-1]
crowd_test(names)

# %%
## Six is a Mob

def crowd_test(nbr_people):
    if len(nbr_people) > 5:
        print('We cannot respect barrier gestures here! (%sp)' % len(nbr_people))
    elif len(nbr_people) >= 3 and len(nbr_people) < 5:
        print('there is a lot of people here! (%sp)' % len(nbr_people))
    elif len(nbr_people) > 0 and len(nbr_people) <= 2: 
        print('there is not a lot of people here! (%sp)' % len(nbr_people))
    elif len(nbr_people) == 0 :
        print('the room is empty! (%sp)' % len(nbr_people))

names=['jacques','henry','david','paul','richard','claire']
crowd_test(names)
del names[-1]
del names[-1]
crowd_test(names)
del names[-1]
crowd_test(names)
del names[-1]
crowd_test(names)
del names[-1]
crowd_test(names)
del names[-1]
crowd_test(names)
# %%
