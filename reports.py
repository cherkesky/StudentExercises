import sqlite3
from student import Student
from cohort import Cohort
from exercise import Exercise

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/cherkesky/workspace/python/StudentExercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student (row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()
            db_cursor.execute("""
            select 
                s.Id,
                s.First_Name,
                s.Last_Name,
                s.Slack,
                s.Cohort_Id,
                c.Name
            from Student s
            join Cohort c on s.Cohort_Id=c.id
            order by s.Cohort_Id
            """)

            all_students = db_cursor.fetchall() # list of tuples
           # print (all_students)

            # for student in all_students:
            #   print(f'{student[1]} {student[2]} is in {student[5]}')
            # for student in all_students:
            #     print(
            #         f'{student.first_name} {student.last_name} is in {student.cohort}')
            for student in all_students:
              print(student)
            ## List comprehension =>
            # [print(s) for s in all_students]  

########################## ALL COHORTS ##########################
class CohortsReport:
  def __init__(self):
    self.db_path = "/Users/cherkesky/workspace/python/StudentExercises/studentexercises.db"

  def all_cohorts(self):
    with sqlite3.connect(self.db_path) as conn:
      conn.row_factory = lambda cursor, row: Cohort (row[1])
      db_cursor = conn.cursor()
      db_cursor.execute("""
      
      select * from Cohort

       """)
      all_cohorts = db_cursor.fetchall()
      #print(all_cohorts)
      for cohort in all_cohorts:
        print(cohort)

########################## ALL EXERCISES ##########################
class ExercisesReport:
  def __init__(self):
    self.db_path = "/Users/cherkesky/workspace/python/StudentExercises/studentexercises.db"

  def all_exercises(self):
    with sqlite3.connect(self.db_path) as conn:
      conn.row_factory = lambda cursor, row: Exercise (row[1], row[2])
      db_cursor = conn.cursor()
      db_cursor.execute("""
      
      select * from Exercise

       """)
      all_exercises = db_cursor.fetchall()
      #print(all_exercises)
      for exercise in all_exercises:
        print(exercise)
########################## JAVASCRIPT EXERCISES ##########################
class JSExercisesReport:
  def __init__(self):
    self.db_path = "/Users/cherkesky/workspace/python/StudentExercises/studentexercises.db"

  def js_exercises(self):
    with sqlite3.connect(self.db_path) as conn:
      conn.row_factory = lambda cursor, row: Exercise (row[1], row[2])
      db_cursor = conn.cursor()
      db_cursor.execute("""
      
      select * from Exercise
      where Exercise_Language = 'JavaScript';

       """)
      js_exercises = db_cursor.fetchall()
      #print(js_exercises)
      for exercise in js_exercises:
        print(exercise)
########################## PYTHON EXERCISES ##########################
class PYExercisesReport:
  def __init__(self):
    self.db_path = "/Users/cherkesky/workspace/python/StudentExercises/studentexercises.db"

  def py_exercises(self):
    with sqlite3.connect(self.db_path) as conn:
      conn.row_factory = lambda cursor, row: Exercise (row[1], row[2])
      db_cursor = conn.cursor()
      db_cursor.execute("""
      
      select * from Exercise
      where Exercise_Language = 'Python';

       """)
      py_exercises = db_cursor.fetchall()
      #print(py_exercises)
      for exercise in py_exercises:
        print(exercise)



print ("################### ALL STUDENTS REPORT ################### ")
reports = StudentExerciseReports()
reports.all_students()
print ("################### COHORTS REPORT ################### ")
cohorts = CohortsReport()
cohorts.all_cohorts()
print ("################### EXERCISES REPORT ################### ")
exercises = ExercisesReport()
exercises.all_exercises()
print ("################### JAVASCRIPT REPORT ################### ")
jsexercises = JSExercisesReport()
jsexercises.js_exercises()
print ("################### PYTHON REPORT ################### ")
pyexercises = PYExercisesReport()
pyexercises.py_exercises()