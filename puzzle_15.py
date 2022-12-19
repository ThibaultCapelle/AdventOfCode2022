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

xmin, xmax=(np.min([np.min([sensor[0] for sensor in sensors]),
                    np.min([beacon[0] for beacon in beacons])]),
            np.max([np.max([sensor[0] for sensor in sensors]),
                    np.max([beacon[0] for beacon in beacons])]))
ymin, ymax=(np.min([np.min([sensor[1] for sensor in sensors]),
                    np.min([beacon[1] for beacon in beacons])]),
            np.max([np.max([sensor[1] for sensor in sensors]),
                    np.max([beacon[1] for beacon in beacons])]))





extra=2000000
beacon_map=np.zeros((xmax-xmin+2*extra, ymax-ymin+2*extra), dtype=np.int8)
def change_coord(coords):
    return [coords[0]-xmin+extra, coords[1]-ymin+extra]

for sensor, beacon in zip(sensors, beacons):
    sensor, beacon=change_coord(sensor), change_coord(beacon)
    beacon_map[sensor[0], sensor[1]]=1
    beacon_map[beacon[0], beacon[1]]=-1
    distance=np.abs(sensor[0]-beacon[0])+np.abs(sensor[1]-beacon[1])
    if (sensor[0]<distance or sensor[1]<distance
        or sensor[0]+distance>=beacon_map.shape[0] or
        sensor[1]+distance>=beacon_map.shape[1]):
        print('problem')
        print([sensor, beacon, distance])
    print([sensor, distance])
    for x in range(sensor[0]-distance,
                   sensor[0]+distance+1):
        for y in range(sensor[1]-distance+np.abs(x-sensor[0]),
                   sensor[1]+distance+1-+np.abs(x-sensor[0])):
            beacon_map[x,y]=2

    
    
