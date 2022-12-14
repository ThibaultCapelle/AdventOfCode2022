#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import os
import numpy as np
filename='input_3'

with open(filename, 'r') as f:
    lines=f.readlines()
choice_value=dict({'X':1,'Y':2,'Z':3})
opponent_dict=dict({'A':1,'B':2,'C':3})
outcome_dict=dict({0:3,1:6,2:0})
current_sum=0
for line in lines:
    line=line.rstrip('\n')
    comp1, comp2 =line[:int(len(line)/2)], line[int(len(line)/2):]
    for i, element in enumerate(comp1):
        out=False
        for j, element2 in enumerate(comp2):
            if element==element2:
                out=True
                break
        if out:
            break
    value=ord(element.lower())-ord('a')+1
    if element.isupper():
        value+=26
    current_sum+=value
print(current_sum)
    