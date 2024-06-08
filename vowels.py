#!/usr/bin/env python3
a = input("enter words contain of vowels:")
count_vowels = 0
vowels = "aeiouAEIOU"
for char in a:
    if char in vowels:
        count_vowels += 1
print("number of vowels:",count_vowels)
