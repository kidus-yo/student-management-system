from students import *


index = 0
running = True


def main_menu():
   print("Welcome to Student Managment System💢")
   print("Main Menu: ")
   print("1. Add Student")
   print("2. Search Student")
   print("3. View Student")
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

   students_list.append(students)
            
def search_student(running, index):
   number = int(input("Enter the ID of the student: "))
   while running:     
    if number != students_list[index]["ID"]:
      index+=1
    elif number == students_list[index]["ID"]:
      
      print(f"Student Name: {students_list[index]["name"]}")
      print(f"ID: {students_list[index]["ID"]}")
      print(f"Age: {students_list[index]["age"]}")
      print(f"Department: {students_list[index]["department"]}")
      print(f"Math Grade: {students_list[index]["math"]}")
      print(f"Physics Grade: {students_list[index]["physics"]}")
      print(f"Chemistry Grade: {students_list[index]["chemistry"]}")
      print(f"Programming Grade: {students_list[index]["programming"]}")
      running = False
      break
    else:
      print("Not Found!❌")
      break
    
def view_stidents():
 for students in students_list:
   print(f"name: {students["name"]} ")
   print(f"ID: {students["ID"]}")
   print(f"Age: {students["age"]}")
   print(f"Department: {students["department"]}")
   print("-" * 30)

def update_student():
   update = int(input("Enter the ID of the student you want to update: "))