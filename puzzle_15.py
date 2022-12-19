#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import numpy as np
filename='input_15'

with open(filename, 'r') as f:
    lines=f.readlines()


sensors, beacons=[], []
for line in lines:
    sensor, beacon=line[:-1].split(':')
    sensor=sensor.lstrip('Sensor at ')
    beacon=beacon.lstrip(' closest beacon is at ')
    x_sensor, y_sensor=sensor.split(', ')
    x_beacon, y_beacon=beacon.split(', ')
    sensors.append([int(x_sensor[2:]),
                    int(y_sensor[2:])])
    beacons.append([int(x_beacon[2:]),
                    int(y_beacon[2:])])


        

nodes=[]
class Node:
    
    def __init__(self, sensor, beacon):
        self.sensor=sensor
        self.beacon=beacon
        self.distance=np.abs(self.sensor[0]-self.beacon[0])+\
            np.abs(self.sensor[1]-self.beacon[1])
        point1, point2=([self.sensor[0], self.sensor[1]+self.distance],
                        [self.sensor[0], self.sensor[1]-self.distance])
        new_point1, new_point2=self.rotate(point1), self.rotate(point2)
        self.range=[new_point2[0], new_point2[1],
                    new_point1[0], new_point1[1]]
    
    def inside(self, point):
        return point[0]>=self.range[0] and point[0]<=self.range[2] and\
            point[1]>=self.range[1] and point[1]<=self.range[3]
    
    def in_range(self, point):
        point=self.unrotate(point)
        return (point[0]<=4000000 and point[0]>=0 
                and point[1]<=4000000 and point[1]>=0)
    
    def rotate(self, point):
        return [point[0]+point[1], point[1]-point[0]]
    
    def unrotate(self, point):
        assert (point[0]+point[1])%2==0
        assert (point[0]-point[1])%2==0
        return [int((point[0]-point[1])/2), 
                int((point[1]+point[0])/2)]
    
    def neghbours(self):
        res=[[self.range[0]-1,i] for i in range(self.range[1],
                                               self.range[3]+1)]
        res+=[[self.range[2]+1,i] for i in range(self.range[1],
                                               self.range[3]+1)]
        res=[[i,self.range[1]-1] for i in range(self.range[0],
                                               self.range[2]+1)]
        res+=[[i,self.range[3]+1] for i in range(self.range[0],
                                               self.range[2]+1)]
        return res
                   

        
for sensor, beacon in zip(sensors, beacons):
    nodes.append(Node(sensor, beacon))
for node in nodes:
    for neighbour in node.neghbours():
        out=False
        for node_bis in nodes:
            if node_bis.inside(neighbour):
                out=True
                break
        if not out:
            if node.in_range(neighbour):
                x, y =node.unrotate(neighbour)
                print(x*4000000+y)
                break
            
            

    
