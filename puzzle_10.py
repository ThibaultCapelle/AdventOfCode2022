#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import numpy as np
filename='input_10'

with open(filename, 'r') as f:
    lines=f.readlines()
X=1
current_cycle=0
targets=[20, 60, 100, 140, 180, 220]
X_vals=[]
for line in lines:
    if 'noop' in line:
        current_cycle+=1
        if current_cycle in targets:
            X_vals.append(X*current_cycle)
    else:
        assert 'addx' in line
        value=int(line[:-1].split(' ')[1])
        current_cycle+=1
        if current_cycle in targets:
            X_vals.append(X*current_cycle)
        current_cycle+=1
        if current_cycle in targets:
            X_vals.append(X*current_cycle)
        X+=value

print(np.sum(X_vals))
# 18240 is too high