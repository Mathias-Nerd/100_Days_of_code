#100 Days of Code
#Author: Mathias Nerd
#A grading program using dictionaries

students_scores = {
    "Mathias" : 81,
    "Sodiq" : 78,
    "Blessing" : 99,
    "Evidence" : 74,
    "David" : 62,
}

students_grade = {}

for item in students_scores:
    print(item)
    score = students_scores[item]
    match score:
        case s if (91 <= score <= 100):
            students_grade[item] = "Outstanding"
        case s if (81 <= score <= 90):
            students_grade[item] = "Exceeds Expectation"
        case s if (71 <= score <= 80):
            students_grade[item] = "Acceptable"
        case _:
            students_grade[item] = "Fail"

print(students_grade)





