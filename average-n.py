#!/usr/bin/env python3
a = input("enter the digits separated by spaces:")
l = list(map(int, a.split()))
s = sum(l)
n =len(a)
avg = s/n
print("average of digits is:",avg)
