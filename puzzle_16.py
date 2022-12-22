#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import numpy as np
filename='input_16_test'

with open(filename, 'r') as f:
    lines=f.readlines()

class Valve:
    
    def __init__(self, rate, childs):
        self.rate=rate
        self.childs=childs

class Graph:
    
    def __init__(self, valves, valve_ini, time_left=30):
        self.valves=valves
        self.valve_ini=valve_ini
        self.time_left=time_left
        self.target_valves=dict()
        for key, val in self.valves.items():
            if val.rate>0:
                self.target_valves[key]=val
    
    def start(self):
        known_path=dict()
        return self.take_decision(self.valves,
                                  self.target_valves,
                                  known_path,
                                  [self.valve_ini],
                                  [self.valve_ini],
                                  self.time_left, 0, 0)
    
    
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
    
    def take_single_decision(self, valves, target_valves,
                             known_paths, pos, time_left,
                             pressure_released,
                             accumulated_release):
        print('===============single decision==================')
        if time_left<=0:
            return accumulated_release
        outputs=[accumulated_release+time_left*pressure_released]
        for key, val in target_valves.items():
            if not (pos, key) in known_paths.keys():
                known_paths[(pos, key)]=self.find_path(pos, key)
            path=known_paths[(pos, key)]
            if len(path)+1<time_left:
                target_valves.pop(key)
                outputs.append(self.take_single_decision(valves,
                                                  target_valves.copy(),
                                                  known_paths.copy(),
                                                  key,
                                                  time_left-len(path), 
                                                  pressure_released+\
                                                      val.rate,
                                                  accumulated_release+\
                                                      len(path)*pressure_released))
                target_valves[key]=val
        return np.max(outputs)
        
    def take_decision(self, valves, target_valves,
                      known_paths, current_pos1,
                      current_pos2,
                      time_left,
                      pressure_released,
                      accumulated_release):
        if len(current_pos1)>1 and len(current_pos2)>1:#we and the elephant are moving
            current_pos1.pop(0)
            current_pos2.pop(0)
            return self.take_decision(valves.copy(), 
                                      target_valves.copy(),
                                      known_paths.copy(),
                                      current_pos1.copy(), current_pos2.copy(),
                                      time_left-1, pressure_released,
                                      accumulated_release+pressure_released)
        else:#one at least needs to take a decision
            outputs=[accumulated_release+time_left*pressure_released]
            if len(current_pos1)>1:#the elephant needs to decide, we keep moving
                print('the elephant needs to decide, we keep moving, pos are: {:},{:}'.format(current_pos1,
                                                                                                   current_pos2))
                current_pos1.pop(0)
                pos2=current_pos2.pop(0)
                for key2, val2 in target_valves.items():
                    if not (pos2, key2) in known_paths.keys():
                        known_paths[(pos2, key2)]=self.find_path(pos2, key2)
                    path2=known_paths[(pos2, key2)]

                    if len(path2)+1<time_left:
                        targets=target_valves.copy()
                        targets.pop(key2)
                        outputs.append(self.take_decision(valves,
                                                          targets,
                                                          known_paths.copy(),
                                                          current_pos1.copy(),
                                                          path2[1:].copy(),
                                                          time_left-1, 
                                                          pressure_released+\
                                                              valves[pos2].rate,
                                                          accumulated_release+\
                                                              pressure_released))
                return np.max(outputs)
            elif len(current_pos2)>1:#We need to decide, the elephant keeps moving
                print('We need to decide, the elephant keeps moving')
                current_pos2.pop(0)
                pos1=current_pos1.pop(0)
                for key1, val1 in target_valves.items():
                    if not (pos1, key1) in known_paths.keys():
                        known_paths[(pos1, key1)]=self.find_path(pos1, key1)
                    path1=known_paths[(pos1, key1)]
                    if len(path1)+1<time_left:
                        targets=target_valves.copy()
                        targets.pop(key1)
                        
                        outputs.append(self.take_decision(valves,
                                                          targets,
                                                          known_paths.copy(),
                                                          path1[1:].copy(),
                                                          current_pos2.copy(),
                                                          time_left-1, 
                                                          pressure_released+\
                                                              valves[pos1].rate,
                                                          accumulated_release+\
                                                              pressure_released))
                return np.max(outputs)
            else:#we both need to take a decision
                print('we should both take a decision')
                pos1=current_pos1.pop(0)
                pos2=current_pos2.pop(0)
                for key1, val1 in target_valves.items():
                    for key2, val2 in target_valves.items():
                        if key2!=key1:
                            if not (pos1, key1) in known_paths.keys():
                                known_paths[(pos1, key1)]=self.find_path(pos1, key1)
                            path1=known_paths[(pos1, key1)]
                            if not (pos2, key2) in known_paths.keys():
                                known_paths[(pos2, key2)]=self.find_path(pos2, key2)
                            path2=known_paths[(pos2, key2)]
                            if len(path1)+1>time_left and len(path2)+1<time_left:
                                targets=target_valves.copy()
                                targets.pop(key2)
                                outputs.append(self.take_single_decision(
                                    valves,
                                    targets,
                                    known_paths.copy(),
                                    key2, time_left-len(path2),
                                    pressure_released+valves[pos2].rate+\
                                        valves[pos1].rate,
                                    accumulated_release+len(path2)*pressure_released))
                            elif len(path1)+1<time_left and len(path2)+1>time_left:
                                targets=target_valves.copy()
                                targets.pop(key1)
                                outputs.append(self.take_single_decision(
                                    valves,
                                    targets,
                                    known_paths.copy(),
                                    key1, time_left-len(path1),
                                    pressure_released+valves[pos2].rate+\
                                        valves[pos1].rate,
                                    accumulated_release+len(path1)*pressure_released))
                            else:
                                targets=target_valves.copy()
                                targets.pop(key1)
                                targets.pop(key2)
                                outputs.append(
                                    self.take_decision(valves,
                                            targets,
                                            known_paths.copy(),
                                            path1[1:].copy(),
                                            path2[1:].copy(),
                                            time_left-1,
                                            pressure_released+valves[pos2].rate+\
                                                valves[pos1].rate,
                                            accumulated_release+pressure_released))
                return np.max(outputs)
        
    
        
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