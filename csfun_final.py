# Developing attendance tracker using Python language for CSFun cw1

student_data = {}

def add_student():
  # here a new student id can be added
  while True:
    student_id = input("Enter student ID (e.g., 0001): ")
    if len(student_id) == 4 and student_id.isdigit():
      # len here returns number of items in an object
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

    date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    # zfill will add needed zero's at the beginning in order to make it 2-digit.

    if validate_date(date):
      student_id = input("Enter the student ID: ")
      attempts = 2 # Allow two attempts to enter the correct student ID, because teacher is also a human being and can make a mistake and it will be time consuming to coming back to the main menu after every mistake.

      while attempts > 0:
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
          attempts -= 1
          if attempts > 0:
            student_id = input("Student ID not found. Please try again: ")
          else:
            print("Too many incorrect student IDs. Returning to main menu.")
            return 

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

def calculate_attendance_summary(student_id):
  # this feature gives us an opportunity to see an attendance summary of a particular student, how many absent and present days in total student have.
  present_days = 0
  absent_days = 0

  for _, status in student_data[student_id]:
    if status == "P":
      present_days += 1
    elif status == "A":
      absent_days += 1

  return present_days, absent_days

def display_attendance_summary():
  # it is almost the same as previous feature but here teacher can see number of absent and present days for all students
  if student_data:
    for student_id in student_data:
      present_days, absent_days = calculate_attendance_summary(student_id)
      print(f"Student ID {student_id}: Present Days = {present_days}, Absent Days = {absent_days}")
  else:
    print("No students added yet.")

def validate_date(date_str):
  
  try:
    year, month, day = map(int, date_str.split('-'))
    # map here needed to apply int for every element
    
    import datetime
    datetime.date(year, month, day)
    return True
  except ValueError:
    return False

def main():
  
  while True:
    print("\nAttendance Tracker Menu:")
    print("1. Mark Today's Attendance")
    print("2. View Attendance Records")
    print("3. Add New Student")
    print("4. Display Attendance Summary")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
      mark_attendance()
    elif choice == '2':
      view_attendance()
    elif choice == '3':
      add_student()
    elif choice == '4':
      display_attendance_summary()
    elif choice == '5':
      print("Exiting the program...")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")
      # elif is been used because we have several conditions

if __name__ == "__main__":
  main()

