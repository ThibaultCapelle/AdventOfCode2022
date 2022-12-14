#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import os
import numpy as np
filename='input_2'

with open(filename, 'r') as f:
    lines=f.readlines()
choice_value=dict({'X':1,'Y':2,'Z':3})
opponent_dict=dict({'A':1,'B':2,'C':3})
outcome_dict=dict({0:3,1:6,2:0})
current_sum=0
for line in lines:
    opponent, me=line.rstrip('\n').split(' ')
    current_sum+=choice_value[me]
    fight_outcome=(choice_value[me]-opponent_dict[opponent])%3
    current_sum+=outcome_dict[fight_outcome]

print(current_sum)
choice_value=dict({'X':0,'Y':3,'Z':6})
fight_outcome_list=[1,2,3]
current_sum=0
for line in lines:
    opponent, me=line.rstrip('\n').split(' ')
    current_sum+=choice_value[me]
    corrected_index=choice_value[me]/3-1
    fight_outcome_index=(opponent_dict[opponent]-1+corrected_index)%3
    fight_outcome=fight_outcome_list[fight_outcome_index]
    current_sum+=fight_outcome
print(current_sum)