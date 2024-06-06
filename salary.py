#!/usr/bin/env python3
b = int(input("enter basic salary:"))
dp = 0.5*b
da = 0.35*(b + dp)
hra =0.08*(b + dp)
ma = 0.03*(b + dp)
pf = 0.1*(b + dp)
salary = b + da +hra +ma -pf
print("original salary:",salary)

