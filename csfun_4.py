def main():
#should be something listed in menu like first choice, second choice..

    choice = input("Enter your choice (1-4): ")



student_data = {}

def add_student():
  # here a new student id can be added
  while True:
    student_id = input("Enter student ID (e.g., 0001): ")
    if len(student_id) == 4 and student_id.isdigit():
      
      if student_id not in student_data:
        student_data[student_id] = [] 

        print(f"Student with ID {student_id} successfully added to the list of students ID's.")
        break
      else:
        print("This ID already exists. Please enter a different one.")
    else:
      print("Invalid student ID. Please enter a 4-digit number.")
# we decided to use specific ID number for every student instead of storing their full names, because names can repeat.

def mark_attendance():
  
  while True:
    day = input("Enter day (1-31): ")
    month = input("Enter month (1-12): ")
    year = input("Enter year (YYYY): ")
# in order to make entering date more convenient , separated day, month and year used.

   
 if student_id in student_data:
      while True:
            status = input("Enter attendance status (P for Present, A for Absent): ").upper()
       if status == "P" or status == "A":
              student_data[student_id].append((date, status))
              print(f"Attendance marked for student ID {student_id} on {date}.")
           return 
else:
              print("Invalid attendance status. Please enter P or A.")
              # typing the whole word every time would be very time consuming for teachers, so we decided to use initials.


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
      print("None.")
  else:
    print("404 non fpund lol.")

