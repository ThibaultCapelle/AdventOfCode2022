#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""
import numpy as np
filename='input_7'


class Folder:
    
    def __init__(self, name, parent=None):
        self.name=name
        self.size=0
        self.childs=dict()
        self.parent=parent
        self.files=dict()
    
    def get_size(self):
        res=np.sum(list(self.files.values()))
        for child in self.childs.values():
            res+=child.get_size()
        return res
    
    def get_tree(self):
        res=[self]
        if len(self.childs)==0:
            return res
        else:
            for child in self.childs.values():
                res+=child.get_tree()
            return res

with open(filename, 'r') as f:
    lines=f.readlines()


father=None
files=dict()
current=None
for line in lines:
    print(line[:-1])
    if father is not None:
        print(current.name)
        print(len(father.childs))
    print('\n')
    if line.startswith('$ cd '):
        if line.endswith('..\n'):
            current=current.parent
        else:
            name=line[:-1].split('cd ')[1]
            if current is None:
                father=Folder(name)
                current=father
            else:
                current=current.childs[name]
    elif line.startswith('$ ls'):
        pass
    else:
        if line.startswith('dir'):
            dirname=line[4:-1]
            if dirname not in current.childs.keys():
                current.childs[dirname]=Folder(dirname, parent=current)
        else:
            size, filename=line[:-1].split(' ')
            current.files[filename]=int(size)

current_sum=0
dirs=father.get_tree()
sizes=dict()
for directory in dirs:
    sizes[directory]=directory.get_size()
total_size=father.get_size()
limit=70000000
free_space=limit-total_size
space_to_free = 30000000-free_space
minimum=np.inf
dir_min=None
for directory in dirs:
    if sizes[directory]>space_to_free and sizes[directory]<minimum:
        minimum=sizes[directory]
        dir_min=directory

print(dir_min.name)
