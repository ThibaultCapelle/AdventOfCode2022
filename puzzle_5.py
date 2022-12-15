#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import numpy as np
filename='input_5'

with open(filename, 'r') as f:
    lines=f.readlines()
for i, line in enumerate(lines):
    if line=='\n':
        break
N=i-1
M=int(len(lines[0])/4)
keys=lines[i-1][:-1].split('  ')
stacks=dict()
for k in keys:
    stacks[k[1]]=[]
j=N-1
while(j>=0):
    print(stacks)
    print(lines[j])
    for k in range(M):
        if lines[j][4*k+1]!=' ':
            stacks[str(k+1)].append(lines[j][4*k+1])
            
    j-=1

for line in lines[N+2:]:
    quantity=line[5:].split(' from ')[0]
    src=line[5:].split(' from ')[1].split(' to ')[0]
    dst=line[5:].split(' from ')[1].split(' to ')[1][0]
    print([quantity, src, dst])
    for i in range(int(quantity)):
        if len(stacks[src])>0:
            stacks[dst].append(stacks[src].pop())
        else:
            print('problem')
            1/0

for val in stacks.values():
    if len(val)>0:
        print(val[-1])
    else:
        print('problem')