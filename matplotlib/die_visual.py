#!/usr/bin/python
# -*- coding:utf-8 -*-

import pygal
from die import Die

die=Die()                #创建一个D6

results=[]               #掷几次骰子，并将结果存储在一个列表中
for roll_num in range(100):
     result=die.roll()
     results.append(result)

frequencies=[]

for value in range(1,die.num_sides+1):
     frequency=results.count(value)
     frequencies.append(frequency)

#print(results)
#print(frequencies)
hist=pygal.Bar()

hist.title="Results of rolling one D6 100 times"
hist.x_labels=['1','2','3','4','5','6']
hist.x_title="Results"
hist.y_title="Frequency of Resuslt"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')