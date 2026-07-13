from students import *
index = 0
def main_menu():
   print("Welcome to Student Managment System💢")
   print("Main Menu: ")
   print("1. Add Student")
   print("2. View Student")
   print("3. Search Student")
   print("4. Update Student")
   print("5. Delete Student")
   print("6. View top Student")
   print("7. View Lowest Student")
   print("8. Calculate Class average")
   print("9. Total Students")
   print("10. Clear Records")
   print("11. Exit")

   choice = int(input("Please Enter your choice?: "))
   return choice

def add_student():
   name = input("Enter Name: ")
   student_ID = int(input("Enter an ID: "))
   age = int(input("Enter age: "))
   department = input("Enter department: ")
   math = input("Enter Math grade: ")
   physics = int(input("Enter Physics grade: "))
   chemistry = int(input("Enter Chemistry grade: "))
   programming = int(input("Enter Programming grade: "))

   students = {"name": name,
            "ID" : student_ID,
            "age" : age,
            "department": department,
            "math": math,
            "physics": physics,
            "chemistry": chemistry,
            "programming": programming, 
            }

   studnets_list.append(students)
            
def search_student():
   id = int(input("Enter the ID of the student: "))

   
