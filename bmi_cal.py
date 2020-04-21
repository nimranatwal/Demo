# Assignments - 1
"""
Name: 
    Adult Body Mass Index Calculator         
Filename:
    bmi_cal.py
Problem Statement:
    Assuming your weight in kilogram and height in meters  
    Calculate your BMI value and print it ?
    Take the height and weight of the user from input 
Hint: 
    How to caltulate your BMI ?
    Divide your weight in kilograms (kg) by your height in metres (m)
    Then divide the answer by your height again to get your BMI
""" 

#my code
print("Calculate your BMI");
w = input("Enter your weight in kg: ")
w = float(w)
h = input("Enter your height in meters: ")
h = float(h)
BMI = (w/h)/h
print("Your BMI is: ")
print(BMI)



#solution code
"""
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
BMI_value = (weight/height)/height
print("BMI value is: " + str(round(BMI_value,2)))


BMI_value = 17.4567
round(BMI_value,2)


"""