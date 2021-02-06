Total_Tickets , Booked = 100,34
PNR , Name = "",""
Source , Destination = "",""
Available = Total_Tickets - Booked
cancel , book = 0 , 0
while True:
    print("1.Check Availibility\n2.Book Tickets\n3.Check Status\n4.Cancel Ticket\n5.Print Ticket\n6.Exit")
    choice = int(input("Enter your choice:- "))

    if(choice == 1):
        print("Available Seats are:- ",Available, ", and Booked Seats are:- ",Booked,"\n")

    elif(choice == 2):
        Book = int(input("How many Tickets you want to Book? "))
        book = Book
        
        if(Book < Available):
            for i in range(Book):
                name = input("Enter Passenger Name:- ")
                Name+=name+" "
                source = input("Enter Source:- ")
                Source+=source+" "
                destination = input("Enter Destination:- ")
                Destination+=destination+" "
                PNR+=str(i)+" "
            Available -= Book
            Booked += Book
            print("Passanger Name:- ",Name,"\nPNR Number of Passanger:- ",PNR)
            print("Source:- ",Source,"\nDestination:- ",Destination)
            print(Book , "Tickets are Booked...!\n")
        else:
            print("Cant book the tickets, ",Available, "Seats remaining only!\n")
        
    elif(choice == 3):
        p = input("Enter your PNR Number:- ")
        if p in PNR:
            print("Ticket is Confirmed..!")
        else:
            print("Ticket is not Confirmed..!")

    elif(choice == 4):
        Cancel = int(input("How many tickets you want to cancel? "))
        cancel = Cancel
        if(Cancel > Book):
            print("Can't cancel the tickets, as you have entered more than booked tickets number\n")
        else:
            if Cancel >= 1:
                for i in range(Cancel):
                    p = input("Enter PNR:- ")
                    n = input("Enter NAME:- ")
                    s = input("Enter SOURCE:- ")
                    d = input("Enter DESTINATION:- ")
                    if p in PNR:
                        PNR = PNR.replace(p,"")
                        Name = Name.replace(n,"")
                        Source = Source.replace(s,"")
                        Destination = Destination.replace(d,"")
                        print("Ticket Cancelled...!\n")
                print(cancel, "Tickets are Cancelled...!\n")
                
            Available += Cancel
            Booked -= Cancel
            Book -=Cancel
                
            
    elif(choice == 5):
        print("\nTotal ",book, "Tickets are booked out of which ", cancel , "Cancelled." )
        print("\nName of Passenger:- ",Name,"\nPNR of Passenger:- ",PNR,"\nSource Point:- ",Source,"\nDestination Point:- ",Destination)
        
    elif(choice == 6):
        print("\nThank you, Visit Again...!\n")
        break

    else:
        print("\nWrong Credentials, Try Again...!\n")
    
