#100 Days of code with python
#Author: Mathias Nerd
#A BMI Calculator
weight = float(input("Enter your weight in Kg "))
height = float(input("Enter your height in m "))
bmi = weight / (height ** 2)
print(round(bmi))