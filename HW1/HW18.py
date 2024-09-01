# The author is Cody Brown, HW18.py

# Write a function that takes the height (unit: inch) and weight (unit: lb) and calculates the body mass 
#index (BMI). Hint: You can find the formula for BMI on its Wikipedia page.

# weight in lbs, height in inches
def bmi(weight, height):
    equation = (weight / (height**2)) * 703
    print(equation)

bmi(150, 70)
