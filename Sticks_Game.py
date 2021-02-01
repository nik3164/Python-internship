print("*********RULES FOR GAME*********\n   1. User must enter the number in between 0 and 5\n   2. User is not allowed to enter any Character or Special Character\n   3. If total number of remaining stick is 1 then Computer Wins.\n")
username = input("Enter your name:- ")
sticks = 21
for i in range(sticks):
    print(username,"enter your number of sticks:- ",end = '')
    user = int(input())
    if(user > 0 and user < 5 ):
        computer = 5-user
        sticks -=(user+computer)
        print("Computer entered the number is :- ",computer)
        print("remaining sticks are:- ",sticks)
        print("\n\n")
    else:
        print("Enter number between 0 and 5")
    if sticks == 1:
        print("computer Win...!")
        break