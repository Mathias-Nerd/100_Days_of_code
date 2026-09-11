#100 Days of code with python
#Author: Mathias Nerd
#Highest score

students_scores = input("Input a list of students scores: ").split()
for i in range(0, len(students_scores)):
    students_scores[i] = int(students_scores[i])
print(students_scores)

maxi = students_scores[0]
for n in range(1, len(students_scores)):
    if students_scores[n] > maxi:
        maxi = students_scores[n]
print(f"The highest score is: {maxi}")