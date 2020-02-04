import sqlite3
from student import Student
from cohort import Cohort

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
            print (all_students)

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
      print(all_cohorts)
      for cohort in all_cohorts:
        print(cohort)

########################## ALL EXERCISES ##########################



reports = StudentExerciseReports()
print ("################### ALL STUDENTS REPORT ################### ")
reports.all_students()
cohorts = CohortsReport()
print ("################### COHORTS REPORT ################### ")
cohorts.all_cohorts()