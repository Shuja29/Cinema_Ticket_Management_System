ticket = []
def addticket():
    confirm = "y"
    while confirm =="y":
        ticket_no = eval(input("Enter your ticket number:"))
        ticket_type = input("Enter your ticket type(royal or classical):")
        timing = input("What is the timing of your ticket?(hh:mm)")
        seat_no = eval(input("Enter your seat number:"))
        ticket.append(ticket_no)
        ticket.append(ticket_type)
        ticket.append(timing)
        ticket.append(seat_no)

        confirm = input("Do you want to add another record?")


def view_tic():
    print("Ticket Number","\tTicket Type","\tTiming","\tSeat Number")
    for i in range(0,len(ticket),4):
        print(format(ticket[i],"10"),"\t",format(ticket[i+1],"8"),"\t",format(ticket[i+2],"8"),"\t",ticket[i+3])

def search_tic():
    ticket_no = eval(input("Enter the ticket number you want to search:"))
    print("Ticket Number","\tTicket Type", "\tTiming", "\tSeat Number")
    for i in range(0,len(ticket),4):
        if ticket_no == ticket[i]:
            print(format(ticket[i], "10"), "\t", format(ticket[i + 1], "8"), "\t", format(ticket[i + 2], "8"), "\t",ticket[i + 3])
        if ticket_no not in ticket:
            print("Record not found")
def update_tic():
    confirm = "y"
    while confirm == "y":
        ticket_no = eval(input("Enter the ticket number you want to update:"))
        for i in range(0, len(ticket), 4):
            if ticket_no == ticket[i]:
             choice = eval(input("What do you want to update? \nEnter the number according to your choice: 1. Ticket Type 2. Timing 3. Seat Number "))
             if choice == 1:
                 ticket[i+1] = input("Enter the new type of ticket:")
             elif choice == 2:
                 ticket[i+2] = input("Enter new timing:")
             elif choice == 3:
                ticket[i+3] = input("Enter new seat number:")
             else:
                break
        confirm = input("Do you want to update another record")
