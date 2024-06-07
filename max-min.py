#!/usr/bin/env python3
n = input("enter numbers separate by ',':")
l = list(n.split(','))

min_value = min(l)
max_value = max(l)
print("minmum value:",min_value)
print("maximum value:",max_value)
