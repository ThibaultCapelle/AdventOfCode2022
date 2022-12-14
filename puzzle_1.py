#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import os
import numpy as np
filename='input_1'

with open(filename, 'r') as f:
    lines=f.readlines()
elves=[]
current_sum=0
for line in lines:
    if line=='\n':
        elves.append(current_sum)
        current_sum=0
    else:
        current_sum+=int(line)
res=0
for i in range(3):
    res+=elves.pop(np.argmax(elves))
print(res)