#100 Days of code with python
#Author: Mathias Nerd
#Leap year program
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap")
        else:
            print("Not leap")
    else:
        print("Leap")
else:
    print("NOt leap")