from students import *


index = 0
running = True
count_student = 1
total1 = 0

count = 0

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

def add_student(count_student):
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
   count_student+=1
   print(f"{count_student}")        
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

def update_student(index, running):
  update = int(input("Enter the ID of the student you want to update: "))
  while running:
   if update == students_list[index]["ID"]:
     
     name = input("Enter Name: ")
     student_ID = int(input("Enter an ID: "))
     age = int(input("Enter age: "))
     department = input("Enter department: ")
     math = input("Enter Math grade: ")
     physics = int(input("Enter Physics grade: "))
     chemistry = int(input("Enter Chemistry grade: "))
     programming = int(input("Enter Programming grade: "))

     students_list[index]["name"] = name
     students_list[index]["ID"] = student_ID
     students_list[index]["age"] = age
     students_list[index]["department"] = department
     students_list[index]["math"] = math
     students_list[index]["physics"] = physics
     students_list[index]["chemistry"] = chemistry
     students_list[index]["programming"] = programming

     print(f"Student Updated Successfully✅")
     
     running = False
     break;
   elif update != students_list[index]["ID"]:
     index+=1
   else:
     print("Student NOT Found❌")

def delete_student(index, running):
  
  delete = int(input("Enter the id of the student you want to delete: "))
  while running:
   if delete == students_list[index]["ID"]:
     students_list.pop(index)
     print("Student Deleted Successfully!✅")
     running = False
     break
   elif delete != students_list[index]["ID"]:
     index+=1
   else:
     print("Student NOT found!‼️")

def top_student(index, count):
 while count < len(students_list):
   grade1 =  int(students_list[index]["math"])
   grade2 =  int(students_list[index]["physics"])
   grade3 =  int(students_list[index]["chemistry"])
   grade4 =  int(students_list[index]["programming"])

   
   sum_total = grade1 + grade2 + grade3 + grade4
   average = sum_total / 4
   total.append(sum_total)
   max_index = total.index(max(total))
   print(f"Top Student: {students_list[max_index]["name"]}#1️⃣")
   print(f"Average: {average}")
   count+=1
   index+=1

def lowest_student(index, count):
  while count < len(students_list):
   grade1 =  int(students_list[index]["math"])
   grade2 =  int(students_list[index]["physics"])
   grade3 =  int(students_list[index]["chemistry"])
   grade4 =  int(students_list[index]["programming"])

   
   sum_total = grade1 + grade2 + grade3 + grade4
   average = sum_total / 4
   total.append(sum_total)
   max_index = total.index(min(total))
   print(f"Lowest: {students_list[max_index]["name"]}🤒")
   print(f"Average: {average}%")
   count+=1
   index+=1

def class_average(index, count, total1):
    while count < len(students_list):
      grade1 =  int(students_list[index]["math"])
      grade2 =  int(students_list[index]["physics"])
      grade3 =  int(students_list[index]["chemistry"])
      grade4 =  int(students_list[index]["programming"])

      
      sum_total = grade1 + grade2 + grade3 + grade4
      average = sum_total / 4
      total_average.append(average)
      count+=1
      index+=1

      for averages in total_average:
       total1 += averages

      average_total = total1/len(total_average)
      print(f"Class Average: {average_total}%")

     
