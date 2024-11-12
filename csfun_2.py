# Attendance tracker for private school 
student_data = {}

def add_student():
  # here a new student id can be added
  while True:
    student_id = input("Enter student ID (e.g., 0001): ")
    if (student_id) == 4 and student_id.isdigit():
    
      if student_id not in student_data:
        student_data[student_id] = [] 

        print(f"Student with ID {student_id} added")
        break
      else:
        print("This ID already exists. Add new")
    else:
      print("Please enter a 4-digit number.")
# we decided to use specific ID number for every student instead of storing their full names, because names can repeat.

def mark_attendance():

    if validate_date(date):
      student_id = input("Enter ID: ")
      
      while attempts > 0:
        if student_id in student_data:
          while True:
            status = input("Enter attendance status (P for Present, A for Absent): ").upper()
        else:
        