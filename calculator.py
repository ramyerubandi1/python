#!/usr/bin/env python3
n1 = float(input("enter first number:"))
operator = input("enter opertor(+,/,*,-):")
n2 = float(input("enter second number:"))
if operator == '+':
    print(n1+n2)
elif operator == '-':
    print(n1-n2)
elif operator == '*':
    print(n1*n2)
elif operator == '/':
    print(n1/n2)
else : 
    print("enter correct operator")
