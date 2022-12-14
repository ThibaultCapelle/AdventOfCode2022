#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import numpy as np
filename='input_4'

with open(filename, 'r') as f:
    lines=f.readlines()
current_sum=0
for line in lines:
    rng1, rng2=line.rstrip('\n').split(',')
    l1,l2=rng1.split('-')
    l3,l4=rng2.split('-')
    if int(l1)<=int(l3) and int(l2)>=int(l4):
        current_sum+=1
    elif int(l1)>=int(l3) and int(l2)<=int(l4):
        current_sum+=1
print(current_sum)
        