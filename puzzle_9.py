#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import numpy as np
filename='input_9'

with open(filename, 'r') as f:
    lines=f.readlines()
    
class Knot:
    
    def __init__(self, parent=None):
        self.parent=parent
        if self.parent is not None:
            self.parent.child=self
        self.child=None
        self.position=[0,0]
        self.visit=dict()
        self.visit[(0,0)]=True
        
    def move(self, direction, quantity):
        for i in range(quantity):
            if direction=='L':
                self.position[1]-=1
            elif direction=='U':
                self.position[0]+=1
            elif direction=='R':
                self.position[1]+=1
            elif direction=='D':
                self.position[0]-=1
            self.follow_head()
    
    def follow_head(self):
        if self.parent is not None:
            dx, dy=(self.parent.position[1]-self.position[1],
                    self.parent.position[0]-self.position[0])
        
            if np.max([np.abs(dx), np.abs(dy)])==2:
                if np.abs(dx)==2:
                    mv_x=int(dx/2)
                else:
                    mv_x=dx
                if np.abs(dy)==2:
                    mv_y=int(dy/2)
                else:
                    mv_y=dy
                self.position[1]+=mv_x
                self.position[0]+=mv_y
                self.mark_new_pos()
        if self.child is not None:
            self.child.follow_head()
    
    def mark_new_pos(self):
        self.visit[tuple(self.position)]=True  
    

class Rope:
    
    def __init__(self, lines, N=10):
        self.knots=[Knot()]
        for i in range(N-1):
            self.knots.append(Knot(parent=self.knots[-1]))
        for line in lines:
            direction, quantity=line[:-1].split(' ')
            quantity=int(quantity)
            self.knots[0].move(direction, quantity)
            print([direction, quantity])
            #self.print_pos()
            print(len(self.knots[-1].visit.keys()))
            
           
    
    def print_pos(self):
        N,M=40, 40
        grid = np.ones((N, M))*(-1)
        for i, knot in enumerate(self.knots):
            if knot.position[0]<int(N/2) and knot.position[1]<int(M/2) \
                and knot.position[0]>-int(N/2) and knot.position[1]>-int(M/2):
                    grid[knot.position[0]+int(N/2), knot.position[1]+int(M/2)]=i
        res=[]
        for i in range(N):
            string=''
            for j in range(M):
                if grid[i,j]==-1:
                    string+='- '
                else:
                    string+=str(int(grid[i,j]))+' '
            res.append(string+'\n')
        for string in res:
                print(string)
        
    
         

puzzle=Rope(lines)
print(len(puzzle.knots[-1].visit.keys()))