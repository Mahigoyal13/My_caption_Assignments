# -*- coding: utf-8 -*-
"""assignment 2 task 2 .py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15J4feMQ3ObpHa2zshK5nsjGMPlHqVJEy
"""

n=10
num_1=0
num_2=1
next_number=num_2
count=1
while count<=n:
  print(next_number,end="")
  count +=1
  num_1,num_2=num_2,next_number
  next_number=num_1+num_2
  print()

list1=[12,-7,5,64,-14]
print([a for j,a in enumerate(list1) if a>=0])

list2=[12,14,-95,3]
print([a for j,a in enumerate(list2) if a>=0])