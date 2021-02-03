Balance = 10000
PIN = 1234
count = 0

while True:
    pin = int(input("Enter PIN(Press 0000 to exit):- "))
    if(pin == PIN):
        transaction = ""
        while True:
            print("1.Deposite\n2.Withdraw\n3.Check Balance\n4.Change PIN\n5.Statment\n6.Exit")
            choice = int(input("Enter your Choice:- "))
            if(choice == 1):
                amount = int(input("Enter the amount:- "))
                print("Amount Added to Accout...!")
                Balance = Balance + amount
                print("Updated Balance is ",Balance)
                transaction += str(amount) + " Added...\n" 
            elif(choice == 2):
                amount = int(input("Enter the amount:- "))
                print("Amount Deducted from Accout...!")
                if(amount > Balance):
                    print("Cant Withdraw...!")
                else:
                    Balance = Balance - amount
                print("Updated Balance is ",Balance)
                transaction += str(amount) + " Deducted....\n"
            elif(choice == 3):
                print("Total Balance is",Balance)
            elif(choice == 4):
                old_pin = int(input("Enter Old PIN:- "))
                if(old_pin == PIN):
                    new_pin = int(input("Enter New PIN:- "))
                    re_new_pin = int(input("Re-Enter your new PIN:- "))
                    if(new_pin == re_new_pin):
                        print("PIN Updated...!")
                        PIN = new_pin
                        break
                    else:
                        print("PIN's not Matched...!")
            elif(choice == 5):
                #break
                
                for i in transaction:
                    if(i == " "):
                                
                        print()
                    else:
                        print(i,end = "")
                print("\nTotal balance:- ",Balance)
            elif(choice == 6):
                break
    else:
        if(pin == 0000):
            break
        print("Invalid Pin...!")
        count +=1
        if(count == 3):
            print("Session Expired...!")
            break
        
    
                
