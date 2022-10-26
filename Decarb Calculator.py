#!/usr/bin/env python
# coding: utf-8

# In[4]:

'''
This is to find how much thca remains after the process

'''
#%%
def total_thc(grams):
    thca = (grams*1000) * potency
    thc = thca * .88
    remaining = thc * .6
    
    return remaining

def num_teaspoons(amount_of_sugar):
    teaspoons = oz * amount_of_sugar
    return teaspoons

def thc_per_teaspoon(num_teaspoons):
    thc_teaspoon = total_thc(grams) / cup2teaspoon(amount_of_sugar)
    return thc_teaspoon

def cup2teaspoon(amount_of_sugar):
    teaspoon = amount_of_sugar * 48
    return teaspoon

def tblsp2teasp(tbspl):
    teasp = tbspl * 3
    return teasp

potency = .18
hot_chocolate = {'Dark Cocoa powder' : 62.4,
                 'Dry Milk' : 120,
                 'Vanilla Coffee Creamer' : 48,
                 'Cannasugar' : 48,
                 'Cinnamon' : 4.5,
                 'Nutmeg' : 1,
                 'Cayenne' : 1.5,
                 'Salt' : 1}

grams = float(input('Enter the total grams of flower: '))
amount_of_sugar = float(input('Enter the amount of sugar in cups: '))
 

print('The total thc is {} mgs'.format(total_thc(grams)))
print('We will have {:.2f} mgs of thc per teaspoon of sugar.'.format(thc_per_teaspoon(cup2teaspoon(amount_of_sugar))))
print('We have {:.2f} number of teaspoons available.'.format(cup2teaspoon(amount_of_sugar)))
#%%
print(cup2teaspoon(1))
print(tblsp2teasp(1.5))
#$$
recipe = 0
for ingredients in hot_chocolate:
    recipe += hot_chocolate[ingredients]
    
print(recipe)
    
'''
As of now, one teaspoon of hot chocolate mix will give us ~3.3 mg of thc. This is after we tally the amount of mix\
, calculate what percentage of the mix is infused sugar, then multiplied by the amount of thc per table spoon.'''
