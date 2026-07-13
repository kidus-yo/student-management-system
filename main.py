#Student Management system
from menu import *

def main():
 while True:
  choice = main_menu()
  if choice == 1:
    add_student()
  elif choice == 2:
   search_student()
  elif choice == 11:
   break
main()