#!/usr/bin/env python3
# Maps for digit to word conversion
units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]

# Get the input from the user
num = input("Enter a number: ")

# Convert the number to words
num = int(num)
if num == 0:
    print("Zero")
else:
    words = ""
    i = 0
    
    while num > 0:
        part = num % 1000
        num //= 1000
        if part > 0:
            words_part = ""
            hundreds = part // 100
            tens_units = part % 100
            
            if hundreds > 0:
                words_part += units[hundreds] + " Hundred "
            
            if tens_units > 0:
                if tens_units < 10:
                    words_part += units[tens_units] + " "
                elif tens_units < 20:
                    words_part += teens[tens_units - 10] + " "
                else:
                    words_part += tens[tens_units // 10] + " "
                    if tens_units % 10 > 0:
                        words_part += units[tens_units % 10] + " "
            
            words = words_part + thousands[i] + " " + words
        
        i += 1
    
    print(words.strip())


