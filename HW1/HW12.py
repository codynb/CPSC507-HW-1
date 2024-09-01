# The author is Cody Brown, HW12.py

# Write a function that takes two parameters for radius and height of a cylinder and prints its volume. 
# Check if your function works correctly by passing 10 and 30 as its arguments. 
# Hint: The volume of a cylinder is the area of the base multiplied by the height of the cylinder.

import math
def cyl_vol(radius, height):
    base_area = math.pi*radius**2
    volume = base_area*height
    print(volume)
    
cyl_vol(10,30)
