# Cohort
# You must define a type for representing a cohort in code.

# The cohort's name (Evening Cohort 6, Day Cohort 26, etc.)
# The collection of students in the cohort.
# The collection of instructors in the cohort.
from nssperson import NSSPerson

class Cohort:
  def __init__ (self, name):
    self.name = name
    self.students = list()
    self.instructors = list()

  def __repr__(self):
      return f'Cohort {self.name}' 
      
  def add_instructor(self, instructor):
    self.instructors.append(instructor)

