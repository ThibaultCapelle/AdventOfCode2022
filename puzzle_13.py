#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import numpy as np
filename='input_13'

with open(filename, 'r') as f:
    lines=f.readlines()
    
class MyList:
    
    def __init__(self, line1, line2):
        self.line1=line1
        self.line2=line2
    
    def compare(self, element1, element2):
        if isinstance(element1, list) or isinstance(element2, list):
            if np.isscalar(element2):
                element2=[element2]
            if np.isscalar(element1):
                element1=[element1]
            for i, item in enumerate(element1):
                if i<len(element2):
                    res=self.compare(item, element2[i])
                    if res!=0:
                        return res
                else:
                    return -1
            if len(element1)<len(element2):
                return 1
            return 0
        elif np.isscalar(element1):
            assert np.isscalar(element2)
            if element1<element2:
                return 1
            elif element1>element2:
                return -1
            else:
                return 0
    
    
i=0
res=[]
while(len(lines)>0):
    i+=1
    line1=eval(lines.pop(0)[:-1])
    line2=eval(lines.pop(0)[:-1])
    if len(lines)>0:
        lines.pop(0)
    print(line1)
    print(line2)
    l=MyList(line1, line2)
    test=l.compare(line1, line2)
    print(test)
    if test==1:
        res.append(i)
    
print(np.sum(res))
    
