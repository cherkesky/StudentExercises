# Exercise
# You must define a type for representing an exercise in code. An exercise can be assigned to many students.

# Name of exercise
# Language of exercise (JavaScript, Python, CSharp, etc.)
# Objective
# The learning objective of this exercise is to practice creating instances of custom types that you defined with class, establishing the relationships between them, and practicing basic data structures in Python.


# Once you have defined all of your custom types, go to main.py, import the classes you need, and implement the following logic.

# Create 4, or more, exercises.
# Create 3, or more, cohorts.
# Create 4, or more, students and assign them to one of the cohorts.
# Create 3, or more, instructors and assign them to one of the cohorts.
# Have each instructor assign 2 exercises to each of the students.

from student import Student
from cohort import Cohort
from instructor import Instructor
from exercise import Exercise

students = list()
exercises = list()

ex1 = Exercise("ChickenMonkey", "JS")
ex2 = Exercise("ChickenMonkey", "Python")
ex3 = Exercise("ChickenMonkey", "Assembly")
ex4 = Exercise("ChickenMonkey", "AI")
ex5 = Exercise("ChickenMonkey", "Binary")
ex6 = Exercise("ChickenMonkey", "Telepathy")

cohort97 = Cohort(97)
cohort98 = Cohort(98)
cohort99 = Cohort(99)

student1 = Student("Guy", "Cherkesky", "@cherkesky", 97)
student2 = Student("Bill", "Gates", "@billyboy", 97)
student3 = Student("Brian", "Chesky", "@bnb_brian", 98)
student4 = Student("Steve", "Balmer", "@whoopie", 99)

inst1 = Instructor("Joe", "Sheperd", "@joe", "Jokes")
inst2 = Instructor("John", "Lemon", "@lemon", "AI")
inst3 = Instructor("Tracy", "Salt", "@salt", "Cakes")

cohort97.add_instructor(inst1)
cohort98.add_instructor(inst2)
cohort99.add_instructor(inst3)

inst1.assign_exercise_to_student(student1, ex1)
inst1.assign_exercise_to_student(student1, ex2)
inst2.assign_exercise_to_student(student1, ex3)
inst2.assign_exercise_to_student(student1, ex4)
inst3.assign_exercise_to_student(student1, ex5)
inst3.assign_exercise_to_student(student1, ex6)

inst1.assign_exercise_to_student(student2, ex1)
inst1.assign_exercise_to_student(student2, ex2)
inst2.assign_exercise_to_student(student2, ex3)
inst2.assign_exercise_to_student(student2, ex4)
inst3.assign_exercise_to_student(student2, ex5)
inst3.assign_exercise_to_student(student2, ex6)

inst1.assign_exercise_to_student(student3, ex1)
inst1.assign_exercise_to_student(student3, ex2)
inst2.assign_exercise_to_student(student3, ex3)
inst2.assign_exercise_to_student(student3, ex4)
inst3.assign_exercise_to_student(student3, ex5)
inst3.assign_exercise_to_student(student3, ex6)

inst1.assign_exercise_to_student(student4, ex1)
inst1.assign_exercise_to_student(student4, ex2)
inst2.assign_exercise_to_student(student4, ex3)
inst2.assign_exercise_to_student(student4, ex4)
inst3.assign_exercise_to_student(student4, ex5)
inst3.assign_exercise_to_student(student4, ex6)


## Challenge 

students = [student1, student2, student3, student4]

for student in students:
  print("")
  i = 0
  print(f'{student.first} is working on:')
  for exercise in student.exercises:
    print(f'{student.exercises[i].name} in {student.exercises[i].language}')
    i = i+1