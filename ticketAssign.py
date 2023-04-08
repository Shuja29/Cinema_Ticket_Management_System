from module01 import *
from module02 import *

# Create an empty list to store ticket assignments
assignment = []

def ticket_assign():
    name = input("Enter the name of movie:")
    if name in movie:
        ticket_no = eval(input("Enter your ticket number:"))
        if ticket_no in ticket:
            start_time = input("Enter the start time of movie(hh:mm):")
            end_time = input("Enter the end time of the movie (hh:mm):")
            assignment.append(name)
            assignment.append(ticket_no)
            assignment.append(start_time)
            assignment.append(end_time)
        else:
            print("Ticket not found")
    else:
        print("Name not found")
    return assignment
def view_assignment():
    print("Movie Name","\tTicket Number","\tStart Time","\tEnd Time")
    for i in range(0, len(assignment), 4):
        print(format(assignment[i],"8"),format(assignment[i+1],"8"),format(assignment[i+2],"6"),assignment[i+3])

