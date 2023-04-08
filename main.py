from module01 import *
from module02 import *
from ticketAssign import *
confirm = "y"
while confirm =="y":
    check = eval(input("1.Movie 2.Ticket 3.Ticket_Assign\nPlease Select : "))
    if check==1:
        print()
        print("Movie Management")
        print()
        choice = eval(input("1. Add 2. View,3. Search 4.Update.\nEnter your choice : "))
        if choice==1:
           addMovie()
        elif choice==2:
           view_mov()
        elif choice==3:
           search_mov()
        elif choice==4:
            update_mov()
        else:
           print("Invalid choice")
    elif check==2:
         print()
         print("Ticket Management")
         print()
         choice = eval(input("1. Add, 2. View,3. Search 4.Update .\nEnter your choice"))
         if choice==1:
            addticket()
         elif choice==2:
            view_tic()
         elif choice==3:
              search_tic()
         elif choice==4:
             update_tic()
         else:
             print("Invalid choice")
    elif check==3:
        print()
        print("Ticket Assign Management")
        print()
        choice =eval(input("Enter your choice \n1.Assign Ticket 2.view assignment"))
        if choice ==1:
            ticket_assign()
        elif choice ==2:
            view_assignment()
    else:
        print("Invalid Choice")
    confirm = input("Press y to repeat the process: ")
