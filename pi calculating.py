# -*- coding: utf-8 -*-
"""
Created on Wed May 23 18:54:20 2018

@author: Ruslan
"""



#calculating pi number by BBP algoritm
from decimal import Decimal, getcontext

n = int(input('Pleas enter the number of digit after decimal point: '))
temp = 0
pi_num = 0
i = 0
getcontext().prec = n + 1

while (i <= 1000000):
    pi_num = decimal.Decimal(((1/16)**i)*((4/(8*i+1))-(2/(8*i+4))-(1/(8*i+5))-(1/(8*i+6))))
    pi_num = temp + pi_num
    temp = pi_num    
    i = i + 1
    
print(pi_num)
print(type(pi_num))  