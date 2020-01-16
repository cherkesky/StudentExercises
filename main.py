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

ex1 = Exercise("ChickenMonkey", "JS")
ex2 = Exercise("ChickenMonkey", "Python")
ex3 = Exercise("ChickenMonkey", "Assembly")
ex4 = Exercise("ChickenMonkey", "AI")

cohort97 = Cohort(97)
cohort98 = Cohort(98)
cohort99 = Cohort(99)

student1 = Student("Guy", "Cherkesky", "@cherkesky", 97)
student2 = Student("Bill", "Gates", "@billyboy", 97)
student3 = Student("Brian", "Chesky", "@bnb_brian", 98)
student4 = Student("Steve", "Balmer", "@whoopie", 99)
