#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import numpy as np
filename='input_8'

with open(filename, 'r') as f:
    lines=f.readlines()


class Mat:
    
    def __init__(self, lines):
        
        self.N, self.M=len(lines), len(lines[0])-1
        self.mat=np.zeros((self.N,self.M))
        
        for i, line in enumerate(lines):
            for j, char in enumerate(line[:-1]):
                self.mat[i,j]=int(char)
    
    def find_max_visibility(self):
        visibilities=np.empty((self.N, self.M))
        for i in range(self.N):
            for j in range(self.M):
                visibilities[i,j]=self.count_visibility(i, j)
        return np.max(visibilities)

    def count_visibility(self, i, j):
        return self.count_visibilit_left(i, j)\
            * self.count_visibilit_right(i, j)\
                * self.count_visibilit_bottom(i, j)\
                    * self.count_visibilit_top(i, j)
    
    def count_visibilit_left(self, i, j):
        if j==0:
            return 0
        else:
            val=self.mat[i,j]
            count=0
            for k in range(j):
                count+=1
                if self.mat[i,j-k-1]>=val:
                    return count
            return count
    
    def count_visibilit_right(self, i, j):
        if j==self.M-1:
            return 0
        else:
            val=self.mat[i,j]
            count=0
            for k in range(j+1, self.M):
                count+=1
                if self.mat[i,k]>=val:
                    return count
            return count
    
    def count_visibilit_top(self, i, j):
        if i==0:
            return 0
        else:
            val=self.mat[i,j]
            count=0
            for k in range(i):
                count+=1
                if self.mat[i-k-1,j]>=val: 
                    return count
            return count
    
    def count_visibilit_bottom(self, i, j):
        if i==self.N-1:
            return 0
        else:
            val=self.mat[i,j]
            count=0
            for k in range(i+1, self.N):
                count+=1
                if self.mat[k,j]>=val:
                    return count
            return count
        

puzzle=Mat(lines)
print(puzzle.find_max_visibility())