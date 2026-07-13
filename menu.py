from students import *
index = 0
running = True
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
            
def search_student(running, index):
   number = int(input("Enter the ID of the student: "))
   while running:     
    if number != studnets_list[index]["ID"]:
      index+=1
    elif number == studnets_list[index]["ID"]:
      
      print(f"Student Name: {studnets_list[index]["name"]}")
      print(f"ID: {studnets_list[index]["ID"]}")
      print(f"Age: {studnets_list[index]["age"]}")
      print(f"Department: {studnets_list[index]["department"]}")
      print(f"Math Grade: {studnets_list[index]["math"]}")
      print(f"Physics Grade: {studnets_list[index]["physics"]}")
      print(f"Chemistry Grade: {studnets_list[index]["chemistry"]}")
      print(f"Programming Grade: {studnets_list[index]["programming"]}")
      running = False
      break
    else:
      print("Not Found!❌")
    

     
