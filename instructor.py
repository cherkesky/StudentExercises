# Instructor
# You must define a type for representing an instructor in code.

# First name
# Last name
# Slack handle
# The instructor's cohort
# The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)

# A method to assign an exercise to a student
from nssperson import NSSPerson


class Instructor(NSSPerson):
  def __init__ (self, first, last, slack, specialty):
    super().__init__(first, last, slack)
    # self.first = first
    # self.last = last
    # self.slack = slack
    self.specialty  = specialty

  def assign_exercise_to_student(self, student_obj, exercise_obj):
    student_obj.exercises.append(exercise_obj)

