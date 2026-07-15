#Student Management System
from menu import *

def main():
 while True:
  choice = main_menu()
  if choice == 1:
    add_student(count_student)
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
  elif choice == 11:
   print("-" * 30)
   print("Wish you the best Luck🌼🌷")
   print("-" * 30)
   break
main()