#Attendance tracker for private school

student_data = {}
# here a new student id can be added
def add_student():
  
  while True:
    student_id = input("Enter student ID (e.g., 0001): ")
    if (student_id) == 4 and student_id():
    
      if student_id not in student_data:
        student_data[student_id] = [] 

        print(f"Student with ID {student_id} successfully added to the list of students ID's.")
        break
      else:
        print("This ID already exists.")
    else:
      print("")
# we decided to use specific ID number for every student instead of storing their full names, because names can repeat.

def attendance



 while attempts > 0:
    if student_id in student_data:
        while True:
            status = input("Enter attendance status (P for Present, A for Absent): ").upper()
      # p fpr present and a for absent, it is more user friendly
     ###    
    #####
   #######
  ######### 
 ########### program should also be able to show all attendance records for students
    else:
          attempts -= 1
     if attempts > 0:
            student_id = input("ID not found.")
else:
            print("Too many incorrect student IDs.")
           
    else:

      print("Invalid date format. Please enter in YYYY-MM-DD format.")

def view_attendance():

  student_id = input("Enter the student ID: ")

  if student_id in student_data:
    print(f"Attendance Records for Student ID {student_id}:")
    if student_data[student_id]: 
      for date, status in student_data[student_id]:
        print(f"Date: {date}, Status: {status}")
    else:
      print("No attendance records found for this student.")
  else:
    print("Student ID not found.")
