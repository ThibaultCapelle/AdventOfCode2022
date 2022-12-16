#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import numpy as np
filename='input_10'

with open(filename, 'r') as f:
    lines=f.readlines()
    

X=1
current_cycle=0
current_writing_pos=0
LCD_lines=[]
current_line=''
for line in lines:
    if 'noop' in line:
        current_cycle+=1
        if np.abs(current_writing_pos-X)<=1:
            current_line+='#'
        else:
            current_line+='.'
        if len(current_line)==40:
            current_writing_pos=0
            LCD_lines.append(current_line)
            current_line=''
        else:
            current_writing_pos+=1
    else:
        assert 'addx' in line
        value=int(line[:-1].split(' ')[1])
        current_cycle+=1
        if np.abs(current_writing_pos-X)<=1:
            current_line+='#'
        else:
            current_line+='.'
        if len(current_line)==40:
            current_writing_pos=0
            LCD_lines.append(current_line)
            current_line=''
        else:
            current_writing_pos+=1
        current_cycle+=1
        if np.abs(current_writing_pos-X)<=1:
            current_line+='#'
        else:
            current_line+='.'
        if len(current_line)==40:
            current_writing_pos=0
            LCD_lines.append(current_line)
            current_line=''
        else:
            current_writing_pos+=1
        X+=value

for line in LCD_lines:
    print(line)