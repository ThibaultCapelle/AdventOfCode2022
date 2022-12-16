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
    
    def count_visibles(self):
        res=0
        for i in range(self.N):
            for j in range(self.M):
                if self.check_visibility(i, j):
                    res+=1
        return res
    
    def check_visibility(self, i, j):
        return self.check_visibilit_left(i, j)\
            or self.check_visibilit_right(i, j)\
                or self.check_visibilit_bottom(i, j)\
                    or self.check_visibilit_top(i, j)
    
    def check_visibilit_left(self, i, j):
        if j==0:
            return True
        else:
            val=self.mat[i,j]
            for k in range(j):
                if self.mat[i,k]>=val:
                    return False
            return True
    
    def check_visibilit_right(self, i, j):
        if j==self.M-1:
            return True
        else:
            val=self.mat[i,j]
            for k in range(j+1, self.M):
                if self.mat[i,k]>=val:
                    return False
            return True
    
    def check_visibilit_top(self, i, j):
        if i==0:
            return True
        else:
            val=self.mat[i,j]
            for k in range(i):
                if self.mat[k,j]>=val:
                    return False
            return True
    
    def check_visibilit_bottom(self, i, j):
        if i==self.N-1:
            return True
        else:
            val=self.mat[i,j]
            for k in range(i+1, self.N):
                if self.mat[k,j]>=val:
                    return False
            return True

puzzle=Mat(lines)
print(puzzle.count_visibles())