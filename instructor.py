# Instructor
# You must define a type for representing an instructor in code.

# First name
# Last name
# Slack handle
# The instructor's cohort
# The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)

# A method to assign an exercise to a student


class Instructor:
  def __init__ (self, first, last, slack, specialty):
    self.first = first
    self.last = last
    self.slack = slack
    self.specialty  = specialty

  def assign_exercise_to_student(self, student_obj, exercise_obj):
    student_obj.exercises.append(exercise_obj)

