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
        opened=dict()
        for key in self.valves.keys():
            opened[key]=False
        return self.take_decision(self.valves,
                                  opened,
                                  self.valve_ini,
                                  self.time_left, 0, 0)
    
    def check_opened(self):
        for valve in self.valves.values():
            if not valve.opened and valve.rate>0:
                return False
        return True
    
    def find_path(self, valve_start, valve_end):
        indices=dict.fromkeys(valves.keys())
        indices_reverse=dict()
        distances=np.ones(len(valves.keys()))*np.inf
        visited=np.array([False]*len(valves.keys()))
        previous=dict()
        for i, key in enumerate(valves.keys()):
            indices[key]=i
            indices_reverse[i]=key
            if key==valve_start:
                distances[i]=0
        current=valve_start
        path=[current]
        while current!=valve_end:
            temp=distances.copy()
            temp[visited]=np.inf
            current=indices_reverse[np.argmin(temp)]
            
            for child in valves[current].childs:
                if not visited[indices[child]]:
                    if distances[indices[child]]>distances[indices[current]]+1:
                        previous[child]=current
                        distances[indices[child]]=distances[indices[current]]+1
            visited[indices[current]]=True
        path=[valve_end]
        current=valve_end
        while current!=valve_start:
            path.append(previous[current])
            current=previous[current]
        return path[::-1]
    
    def take_decision(self, valves, opened, current_pos, time_left,
                      pressure_released,
                      accumulated_release):
        outputs=[accumulated_release+time_left*pressure_released]
        for key, val in valves.items():
            if val.rate>0 and not opened[key]:
                path=self.find_path(current_pos, key)
                if len(path)+1<time_left:
                    opened[key]=True
                    outputs.append(
                        self.take_decision(valves.copy(),
                                opened.copy(),
                                key,
                                time_left-len(path),
                                pressure_released+val.rate,
                                accumulated_release+len(path)*pressure_released))
                    opened[key]=False
        return np.max(outputs)
        
    
    def alpha_beta(self, valves, valve_ini, time_left, pressure_released,
                   accumulated_release):
        if time_left==0:
            return accumulated_release
        else:
            value =-np.inf
            if not valves[valve_ini].opened:#open the valve
                valves[valve_ini].opened=True
                value=np.max([value, self.alpha_beta(valves.copy(),
                                     valve_ini,
                                     time_left-1,
                                     pressure_released+valves[valve_ini].rate,
                                     accumulated_release+pressure_released)])
                valves[valve_ini].opened=False
            if self.check_opened():#do nothing
                value=np.max([value,
                              accumulated_release+\
                                  time_left*pressure_released])
            else:#check the childs
                for child in valves[valve_ini].childs:
                    value=np.max([value, self.alpha_beta(valves.copy(),
                                     child,
                                     time_left-1,
                                     pressure_released,
                                     accumulated_release+pressure_released)])
            return value

        
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
graph=Graph(valves, 'AA', time_left=30)
print(graph.start())