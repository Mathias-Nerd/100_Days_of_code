weight = float(input("Enter your weight in Kg "))
height = float(input("Enter your height in m "))
bmi = weight / (height ** 2)
print(round(bmi))

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are Underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are A normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are Overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are Obese")
else:
    print(f"Your bmi is {bmi}, you are Clinically obese")