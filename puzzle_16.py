#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import numpy as np
filename='input_16'

with open(filename, 'r') as f:
    lines=f.readlines()

class Valve:
    
    def __init__(self, rate, childs):
        self.rate=rate
        self.childs=childs
        self.opened=False

class Graph:
    
    def __init__(self, valves, valve_ini, time_left=30):
        self.valves=valves
        self.valve_ini=valve_ini
        self.time_left=time_left
    
    def start(self):
        return self.alpha_beta(valves,
                               self.valve_ini,
                               self.time_left,
                               0,
                               0)
    
    def alpha_beta(self, valves, valve_ini, time_left, pressure_released,
                   accumulated_release):
        if time_left==0:
            return accumulated_release
        else:
            #open the valve
            if not valves[valve_ini].opened:
                valves[valve_ini].opened=True
                res1=self.alpha_beta(valves.copy(),
                                     valve_ini,
                                     time_left-1,
                                     pressure_released+valves[valve_ini].rate,
                                     accumulated_release+pressure_released)
                valves[valve_ini].opened=False
            else:#do nothing
                res1=self.alpha_beta(valves.copy(),
                                     valve_ini,
                                     time_left-1,
                                     pressure_released,
                                     accumulated_release+pressure_released)
            #try the childs
            res2=[self.alpha_beta(valves.copy(),
                                     child,
                                     time_left-1,
                                     pressure_released,
                                     accumulated_release+pressure_released) 
                  for child in valves[valve_ini].childs]
            return np.max(res2+[res1])
        
valves=dict()
for line in lines:
    valve_name=line[6:8]
    flow_rate=int(line.split(';')[0].split('=')[1])
    if 'valves' in line:
        tunnels=line[:-1].split('valves ')[1]
        tunnels=tunnels.split(', ')
    elif 'valve' in line:
        tunnels=[line[:-1].split('valve ')[1]]
    valves[valve_name]=Valve(flow_rate, tunnels)
graph=Graph(valves, 'AA', time_left=11)
print(graph.start())