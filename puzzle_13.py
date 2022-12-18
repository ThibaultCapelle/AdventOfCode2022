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

class QuickSort:
    
    def __init__(self, table):
        self.table=table
    
    def compare(self, i, j):
        l=MyList(self.table[i], self.table[j])
        return l.compare(self.table[i], self.table[j])==1
    
    def swap(self, i, j):
        temp=self.table[i]
        self.table[i]=self.table[j]
        self.table[j]=temp
    
    def partition(self, first, last, pivot):
        self.swap(pivot, last)
        j=first
        for i in range(first, last):
            if self.compare(i, last):
                self.swap(i, j)
                j+=1
        self.swap(last, j)
        return j
    
    def sort(self, first, last):
        if first<last:
            pivot=np.random.randint(first, last+1)
            pivot=self.partition(first, last, pivot)
            self.sort(first, pivot-1)
            self.sort(pivot+1, last)

res=[]
inputs=[]
for line in lines:
    if line!='\n':
        inputs.append(eval(line[:-1]))
inputs.append([[2]])
inputs.append([[6]])
sort=QuickSort(inputs)
sort.sort(0,len(inputs)-1)

res=[]
for i, item in enumerate(sort.table):
    if item==[[2]] or item==[[6]]:
        res.append(i+1)
print(res[0]*res[1])