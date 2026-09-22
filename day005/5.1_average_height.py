#100 Days of code with python
#Author: Mathias Nerd
#Average height
student_heights = input("Input a list of student heihts: ").split()
sum = 0
length = 0
for n in range(0, len(student_heights)):
    student_heights[n] =  int(student_heights[n])
    sum += student_heights[n]
    length += 1
print(f"sum = {sum}")
print(f"Average = {round(sum/length)}")

