#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:16:10 2022

@author: usera
"""

import numpy as np
filename='input_11'

with open(filename, 'r') as f:
    lines=f.readlines()

class Monkeys:
    
    def __init__(self):
        self.monkeys=dict()
        self.modulo=None
        
    def add_monkey(self, number, items, operation, test, targets):
        self.monkeys[number]=Monkey(items, operation, test, targets, self)
    
    def send_item(self, item, target):
        self.monkeys[target].items.append(item)
        
class Monkey:
    
    def __init__(self, items, operation_text, test_val, targets, parent):
        self.items=items
        self.operation_text=operation_text
        self.parent=parent
        self.test_val=test_val
        self.targets=targets
        self.object_inspected=0
    
    def test(self, val):
        return val%self.test_val==0
    
    def operation(self, val):
        return eval(self.operation_text.replace('old','val'))
    
    def turn(self):
        ids_to_remove=[]
        
        #print('len items is {:}'.format(len(self.items)))
        print(self.items)
        for i, item in enumerate(self.items):
            self.object_inspected+=1
            item=self.operation(item)%self.parent.modulo
            if self.test(item):
                self.send(item, self.targets[0])
            else:
                self.send(item, self.targets[1])
            ids_to_remove.append(i)
        self.items=[self.items[i] for i in range(len(self.items)) 
                    if i not in ids_to_remove]

    def send(self, item, target):
        self.parent.send_item(item, target)
    
    def print_all(self):
        print(self.items)
        print(self.object_inspected)
        
            

monkeys=Monkeys()
for line in lines:
    if line.startswith('Monkey'):
        number = int(line.split(' ')[1][:-2])
        print('\n{:}'.format(number))
    elif line.startswith('  Starting items'):
        items = line[:-1].lstrip('Starting items: ').split(', ')
        items=[int(item) for item in items]
    elif line.startswith('  Operation:'):
        operation = line[:-1].lstrip('  Operation: ').split('=')[1]
        print(operation)
    elif line.startswith('  Test'):
        divider=int(line.lstrip('  Test: divisible by ')[:-1])
        print('divider: {:}'.format(divider))
    elif line.startswith('    If true'):
        target_true=int(line.lstrip('    If true: throw to monkey ')[:-1])
    elif line.startswith('    If false'):
        target_false=int(line.lstrip('    If false: throw to monkey ')[:-1])
        print('targets: {:}'.format([target_true, target_false]))
        monkeys.add_monkey(number, items, operation, divider,
                               [target_true, target_false])

modulo=np.prod([monkey.test_val for monkey in monkeys.monkeys.values()])
monkeys.modulo=modulo
N_round=10000
for i in range(N_round):
    print(i)
    for k, monkey in monkeys.monkeys.items():
        '''print('turn number {:} monkey number {:}'.format(i, k))
        monkey.print_all()
        print([monkey.object_inspected for monkey in monkeys.monkeys.values()])'''
        monkey.turn()


max1=np.max([monkey.object_inspected for monkey in monkeys.monkeys.values()])
maximum=0
for k, monkey in monkeys.monkeys.items():
    if monkey.object_inspected>maximum:
        maximum=monkey.object_inspected
        id_max=k
max_1=monkeys.monkeys.pop(id_max).object_inspected
maximum=0
for k, monkey in monkeys.monkeys.items():
    if monkey.object_inspected>maximum:
        maximum=monkey.object_inspected
        id_max=k
max_2=monkeys.monkeys.pop(id_max).object_inspected
print(max_1*max_2)
        