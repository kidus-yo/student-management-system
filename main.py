#Student Management System
from menu import *

def main():
 while True:
  choice = main_menu()
  if choice == 1:
    add_student()
  elif choice == 2:
   search_student(running, index)
  elif choice == 3:
   view_stidents()
  elif choice == 4:
   update_student(index, running)
  elif choice == 5:
   delete_student(index, running)
  elif choice == 6:
   top_student(index, count)
  elif choice == 7:
   lowest_student(index, count)
  elif choice == 8:
   class_average(index, count, total1)
  elif choice == 9:
   total_students()
  elif choice == 10:
   clear_records()
  elif choice == 11:
   print("-" * 30)
   print("Wish you the best Luck🌼🌷")
   print("-" * 30)
   break
  else:
   print("Please Enter only a valid number(1-11)‼️")
   break
if __name__ == "__main__":
 main()