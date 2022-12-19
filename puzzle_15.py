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





exclusion_lines=dict()
for sensor, beacon in zip(sensors, beacons):
    distance=np.abs(sensor[0]-beacon[0])+np.abs(sensor[1]-beacon[1])
    print(sensor)
    for y in range(sensor[1]-distance,
                   sensor[1]+distance+1):
        if not y in exclusion_lines.keys():
            exclusion_lines[y]=[]
        exclusion_lines[y].append([sensor[0]-distance+np.abs(y-sensor[1]),
                   sensor[0]+distance-np.abs(y-sensor[1])])

def check_a_line(y):
    position_blocked=dict()
    for item in exclusion_lines[y]:
        x1, x2 =item
        for i in range(x1, x2+1):
            position_blocked[i]=True
    for beacon in beacons:
        if beacon[1]==y:
            if beacon[0] in position_blocked.keys():
                position_blocked.pop(beacon[0])
    return len(position_blocked.keys())

print(check_a_line(2000000))
        