#!/usr/bin/env python3

for n in range(1, 1000):
    
    num_str = str(n)
    
    
    sum_of_cubes = 0
    
    
    for digit in num_str:
        
        sum_of_cubes += int(digit) **3
    if sum_of_cubes == n:
        
        print(n)

