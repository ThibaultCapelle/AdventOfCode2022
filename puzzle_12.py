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
        self.distances=np.inf*np.ones(self.mat.shape)
    
    def start(self, i_start, j_start, i_end, j_end):
        self.i_end=i_end
        self.j_end=j_end
        self.visited=np.zeros((N, M))==1
        self.N_visited=0
        self.distances=np.inf*np.ones(self.mat.shape)
        self.distances[i_start,j_start]=0
        self.iterate()
    
    def iterate(self):
        while not self.visited[self.i_end, self.j_end]:
            i, j=self.select_current()
            if i==-1:
                break
            else:
                self.add_connections(i, j)
    
    def select_current(self):
        temp_mat=self.distances.copy()
        temp_mat[self.visited]=np.inf
        i, j = np.unravel_index(np.argmin(temp_mat),
                                temp_mat.shape)
        if np.count_nonzero(temp_mat!=np.inf)==0:
            return (-1, -1)
        else:
            return (i, j)
            
        
    def add_connections(self, i, j):
        self.check_left(i, j)
        self.check_right(i, j)
        self.check_top(i, j)
        self.check_bottom(i, j)
        self.visited[i,j]=True
        self.N_visited+=1
    
    def check_connectivity(self, i, j, k, l):
        self.visited[i,j]=True
        if i==k and j==l:
            return True
        else:
            if self.check_left(i, j):
                res1=self.check_connectivity(i, j-1, k, l)
            else:
                res1=False
            if self.check_right(i, j):
                res2=self.check_connectivity(i, j+1, k, l)
            else:
                res2=False
            if self.check_top(i, j):
                res3=self.check_connectivity(i-1, j, k, l)
            else:
                res3=False
            if self.check_bottom(i, j):
                res4=self.check_connectivity(i+1, j, k, l)
            else:
                res4=False
            
            return res1 or res2 or res3 or res4
    
    def check_left(self, i, j):
        if j!=0:
            if not self.visited[i,j-1]:
                if self.mat[i,j-1]<=self.mat[i,j]+1:
                    self.distances[i,j-1]=np.min([self.distances[i,j-1],
                                                 self.distances[i,j]+1])
                    return True
        return False
    
    def check_right(self, i, j):
        if j!=self.M-1:
            if not self.visited[i,j+1]:
                if self.mat[i,j+1]<=self.mat[i,j]+1:
                    self.distances[i,j+1]=np.min([self.distances[i,j+1],
                                                 self.distances[i,j]+1])
                    return True
        return False
    
    def check_bottom(self, i, j):
        if i!=self.N-1:
            if not self.visited[i+1,j]:
                if self.mat[i+1,j]<=self.mat[i,j]+1:
                    self.distances[i+1,j]=np.min([self.distances[i+1,j],
                                                 self.distances[i,j]+1])
                    return True
        return False
    
    def check_top(self, i, j):
        if i!=0:
            if not self.visited[i-1, j]:
                if self.mat[i-1,j]<=self.mat[i,j]+1:
                    self.distances[i-1,j]=np.min([self.distances[i-1,j],
                                                 self.distances[i,j]+1])
                    return True
        return False
    
'''graph=Graph(mat)
graph.start(0, 0, *end)
'''
graph=Graph(mat)
initial_pos_i, inital_pos_j=np.where(mat==0)
distances=[]
for k, (i, j) in enumerate(zip(initial_pos_i, inital_pos_j)):
    print([i,j])
    #print(graph.check_connectivity(i, j, *end))
    graph.start(i, j, *end)
    distances.append(graph.distances[end[0], end[1]])
print(np.min(distances))
    
        