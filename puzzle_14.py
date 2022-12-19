#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import numpy as np
filename='input_14'

with open(filename, 'r') as f:
    lines=f.readlines()

rocks=np.zeros((700,600))
for line in lines:
    coords_raw=line[:-1].split(' -> ')
    coords=[]
    for i, coord in enumerate(coords_raw):
        x, y = coord.split(',')
        if i>0:
            x1, x2, y1, y2=(np.min([coords[-1][0], int(x)]),
                            np.max([coords[-1][0], int(x)]),
                            np.min([coords[-1][1], int(y)]),
                            np.max([coords[-1][1], int(y)]))
            rocks[x1:x2+1,y1:y2+1]=1
        coords.append([int(x), int(y)])

ylim=np.max(np.unravel_index(np.where(rocks==1), rocks.shape)[1][1])
rocks[:,ylim+2]=1
x_start, y_start=500,0

def propagate(x1, y1):
    if rocks[x1,y1+1]==0:
        return propagate(x1, y1+1)
    elif rocks[x1-1,y1+1]==0:
        return propagate(x1-1, y1+1)
    elif rocks[x1+1,y1+1]==0:
        return propagate(x1+1, y1+1)
    else:
        rocks[x1, y1]=-1
        print([x1,y1])
        return [x1,y1]
        
i=0
while(propagate(x_start, y_start)!=[x_start, y_start]):
    i+=1
print(i+1)
    
