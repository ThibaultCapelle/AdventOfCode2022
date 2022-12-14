#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import numpy as np
filename='input_3'

with open(filename, 'r') as f:
    lines=f.readlines()
current_sum=0
N=int(len(lines)/3)
for i in range(N):
    comp1, comp2, comp3=lines[3*i], lines[3*i+1], lines[3*i+2]
    for element in comp1[:-1]:
        out1, out2=False, False
        for element2 in comp2[:-1]:
            if element==element2:
                out1=True
                break
        if out1:
            for element3 in comp3[:-1]:
                if element3==element2:
                    out2=True
                    break
        if out2:
            break
    print([element, comp1, comp2, comp3])
    value=ord(element.lower())-ord('a')+1
    if element.isupper():
        value+=26
    current_sum+=value
print(current_sum)
    