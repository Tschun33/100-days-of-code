
# list comprehension
from random import randint

with open("file1.txt") as file:
    lines_1 = file.readlines()
#   lines_1 = [line.rstrip() for line in lines_1]

with open("file2.txt") as file:
    lines_2 = file.readlines()
#    lines_2 = [line.rstrip() for line in lines_2]


overlap = [int(number) for number in lines_1 if number in lines_2]
print(overlap)

# dictionary comprehension
names = ["Alex", "Beth", "Caroline"]

student_scores = {student: randint(1,100) for student in names}
print(student_scores)
passed_students = {student: score for (student, score) in student_scores.items() if score > 60}
print(passed_students)