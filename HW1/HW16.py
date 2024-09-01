# The author is Cody Brown, HW16.py

# Write a function that takes time, temp, and ratio and calculates and prints the result of the following 
# formula: Maturity = 23.7 × time3 + temp 273 +ln(ratio)

import math
def maturity(time, temp, ratio):
    formula = 27.3 * time**3 + (temp/273) + math.log(ratio)
    print(formula)

maturity(1,2,3)
