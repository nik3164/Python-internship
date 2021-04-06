data = pd.read_csv("students.csv")
print(data)

while(True):
    print("1. Specific student\n2. Specific class students\n3. Students having marks greater than some threshold(ask "
          "user input)\n4. Count of students in each class\n5. Exit")
    choice = int(input("Enter your choice:- "))

    if(choice == 1):
        name = input("Enter Name:- ")
        print(data.loc[data["Studname"] == name])

    elif(choice == 2):
        Class = input("Enter Class:- ")
        print(data.loc[data["Studclass"] == Class])

    elif(choice == 3):
        marks = int(input("Enter threshold marks:- "))
        print(data.loc[data["Studmarks"] > marks ])

    elif(choice == 4):
        print("Total FE count is:- ",len(data.loc[data["Studclass"] == 'FE']))
        print("Total SE count is:- ", len(data.loc[data["Studclass"] == 'SE']))
        print("Total TE count is:- ", len(data.loc[data["Studclass"] == 'TE']))
        print("Total BE count is:- ", len(data.loc[data["Studclass"] == 'BE']))

    elif(choice == 5):
        break

    else:
        print("Invalid Input...!")