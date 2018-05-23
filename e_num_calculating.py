# -*- coding: utf-8 -*-
"""
Created on Wed May 23 21:21:03 2018

@author: Ruslan
"""

#Calculating e number by Newton's Series
"""from decimal import Decimal, getcontext

temp, e_num, i, x = 0, 0, 0, 0

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else: 
      return x * factorial(x-1)

n = int(input('Pleas enter the number of digit after decimal point: '))

getcontext().prec = n + 1

while (i <= 20):
    e_num = decimal.Decimal(1/factorial(i))
    e_num = temp + e_num
    temp = e_num    
    i = i + 1
    
print(e_num)
print(type(e_num))
"""
# Calculating e number by Brothers' Formulae
from decimal import Decimal, getcontext

temp, e_num, i, x = 0, 0, 0, 0

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else: 
      return x * factorial(x-1)

n = int(input('Pleas enter the number of digit after decimal point: '))

getcontext().prec = n + 1

while (i <= 10):
    e_num = decimal.Decimal((2*i+2)/(factorial(2*i+1)))
    e_num = temp + e_num
    temp = e_num    
    i = i + 1
    
print(e_num)
print(type(e_num))