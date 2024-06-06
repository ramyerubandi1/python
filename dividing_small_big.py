#!/usr/bin/env python3
n1 = float(input("enter first value:"))
n2 = float(input("enter second value:"))
if n1 == 0 and n2 == 0:
    print("give input correctlly:")
else:
    if n1<n2:
        print(n1/n2)
    else:
        print(n2/n1)
