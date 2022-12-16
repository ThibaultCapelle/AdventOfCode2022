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

class Rope:
    
    def __init__(self, lines):
        
        self.visit=dict()
        self.tail=[0,0]
        self.head=[0,0]
        self.visit[(0,0)]=True
        for line in lines:
            direction, quantity=line[:-1].split(' ')
            quantity=int(quantity)
            self.move(direction, quantity)
    
    def move(self, direction, quantity):
        for i in range(quantity):
            if direction=='L':
                self.head[1]-=1
            elif direction=='U':
                self.head[0]+=1
            elif direction=='R':
                self.head[1]+=1
            elif direction=='D':
                self.head[0]-=1
            self.follow_head()
            
    
    def follow_head(self):
        dx, dy=self.head[1]-self.tail[1], self.head[0]-self.tail[0]
        
        if np.max([np.abs(dx), np.abs(dy)])==2:
            if np.abs(dx)==2:
                mv_x=int(dx/2)
            else:
                mv_x=dx
            if np.abs(dy)==2:
                mv_y=int(dy/2)
            else:
                mv_y=dy
            self.tail[1]+=mv_x
            self.tail[0]+=mv_y
            self.mark_new_pos()
    
    def mark_new_pos(self):
        self.visit[tuple(self.tail)]=True       

puzzle=Rope(lines)
print(len(puzzle.visit.keys()))