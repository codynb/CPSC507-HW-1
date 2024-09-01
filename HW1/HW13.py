# The author is Cody Brown, HW13.py

# Craft two functions: the first calculates the area of a circle, and the second determines the area
# of a square. Consider what parameters each function requires. Then, using these functions, create a 
# third that computes the area between a circle nestled within a square.

import math
def circle_area(radius):
    area_c = math.pi*radius**2
    return area_c

def sqr_area(length):
    area_s = length**2
    return area_s

radius = 1
length = 3

cir_area = circle_area(radius)
sqr_area = sqr_area(length)
    
def area_inbetween(cir_area, sqr_area):
    inbetween = sqr_area - cir_area
    print(inbetween)

area_inbetween(cir_area, sqr_area)
