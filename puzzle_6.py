#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""
#wrong=RDRQHLNHS
import numpy as np
filename='input_6'

with open(filename, 'r') as f:
    line=f.read()[:-1]
for i in range(3, len(line)):
    if line[i]!=line[i-1] and line[i]!=line[i-2] and line[i]!=line[i-3] and\
        line[i-1]!=line[i-2] and line[i-1]!=line[i-3] and line[i-2]!=line[i-3]:
            print(line[i-3:i+1])
            print(i+1)
            break

