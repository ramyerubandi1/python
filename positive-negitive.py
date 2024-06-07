#!/bin/usr/env python3
n = input("enter numbers by separating using (,):")
l =list(map(int,n.split(',')))
positives = [num for  num in l if num > 0]
p = len(positives)
negitives = [num for num in l if num < 0]
n = len(negitives)
zero = [num for num in l if num == 0]
z = len(zero)
print ("positive numbers:",p)
print("negitive numbers:",n)
print("zeros:",z)
ass = sorted(l)
print("given numbers in ascending order:",ass)
