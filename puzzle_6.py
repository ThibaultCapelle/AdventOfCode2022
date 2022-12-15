#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""
import numpy as np
filename='input_6'

def is_there_a_pair(line):
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            if line[i]==line[j]:
                return True
    return False

with open(filename, 'r') as f:
    line=f.read()[:-1]
for i in range(13, len(line)):
    if not is_there_a_pair(line[i-13:i+1]):
        print(line[i-13:i+1])
        print(i)
        break
