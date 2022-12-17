#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import numpy as np
filename='input_12'

with open(filename, 'r') as f:
    lines=f.readlines()

N, M=len(lines), len(lines[0])-1
mat=np.zeros((N,M))
start, end=None, None
for i, line in enumerate(lines):
    for j, char in enumerate(line[:-1]):
        if char=='S':
            start=[i,j]
            mat[i,j]=0
        elif char=='E':
            end=[i,j]
            mat[i,j]=25
        else:
            mat[i,j]=ord(char)-ord('a')

class Graph:
    
    def __init__(self, mat):
        self.mat=mat
        self.N, self.M=self.mat.shape
        self.visited=np.zeros((N, M))==1
        self.N_visited=0
        self.distances=np.inf*np.ones((N,M))
        self.nodes=[]
    
    def start(self, i_start, j_start, i_end, j_end):
        self.i_end=i_end
        self.j_end=j_end
        self.distances[i_start,j_start]=0
        self.iterate()
    
    def iterate(self):
        while not self.visited[self.i_end, self.j_end]:
            i, j=self.select_current()
            self.add_connections(i, j)
    
    def select_current(self):
        temp_mat=self.distances.copy()
        temp_mat[self.visited]=np.inf
        i, j = np.unravel_index(np.argmin(temp_mat),
                                temp_mat.shape)
        return (i, j)
            
        
    def add_connections(self, i, j):
        self.check_left(i, j)
        self.check_right(i, j)
        self.check_top(i, j)
        self.check_bottom(i, j)
        self.visited[i,j]=True
        self.N_visited+=1
    
    def check_left(self, i, j):
        if j!=0:
            if not self.visited[i,j-1]:
                if self.mat[i,j-1]<=self.mat[i,j]+1:
                    self.distances[i,j-1]=np.min([self.distances[i,j-1],
                                                 self.distances[i,j]+1])
    
    def check_right(self, i, j):
        if j!=self.M-1:
            if not self.visited[i,j+1]:
                if self.mat[i,j+1]<=self.mat[i,j]+1:
                    self.distances[i,j+1]=np.min([self.distances[i,j+1],
                                                 self.distances[i,j]+1])
    
    def check_bottom(self, i, j):
        if i!=self.N-1:
            if not self.visited[i+1,j]:
                if self.mat[i+1,j]<=self.mat[i,j]+1:
                    self.distances[i+1,j]=np.min([self.distances[i+1,j],
                                                 self.distances[i,j]+1])
    
    def check_top(self, i, j):
        if i!=0:
            if not self.visited[i-1, j]:
                if self.mat[i-1,j]<=self.mat[i,j]+1:
                    self.distances[i-1,j]=np.min([self.distances[i-1,j],
                                                 self.distances[i,j]+1])

graph=Graph(mat)
graph.start(*start, *end)
print(graph.distances[end[0], end[1]])
    
        