import pymysql
con = pymysql.connect(host = "localhost" , user = "root" , password = "root", database = "db_admission")
cur = con.cursor()
user = input("Enter Username:- ")
qry = "SELECT * FROM tbl_admin WHERE user=" + "'" + user + "'"
cur.execute(qry)
User = cur.fetchall()

password = input("Enter Password:- ")
qry1 = "SELECT * FROM tbl_admin WHERE password=" + "'" + password + "'"
cur.execute(qry1)
Password = cur.fetchall()
if(len(User) >=1 and len(Password) >= 1):
    flag = True
else:
    flag = False
con.commit()
con.close()

while(True):
    if(flag == True):
        print("\n1. New Admission\n2. Update Info\n3. Remove Admission\n4. View Admissions\n5. Exit")
        choice = int(input("Enter your Choice:- "))
        if(choice == 1):
            con = pymysql.connect(host = "localhost" , user = "root" , password = "root", database = "db_admission")
            cur = con.cursor()
            name = input("Enter Name:- ")
            Class = input("Enter Class:- ")
            div  = input("Enter Division:- ")
            phoneno = input("Enter Mobile Number:- ")
            address = input("Enter Address:- ")
            qry = "INSERT into db_admission.tbl_admission values (0,'"+name+"','"+Class+"','"+div+"','"+phoneno+"','"+address+"')"
            cur.execute(qry)
            con.commit()
            con.close()
            print("Record Added...!")
            
        elif(choice == 2):
            con = pymysql.connect(host = "localhost" , user = "root" , password = "root", database = "db_admission")
            cur = con.cursor()
            while True:
                print("\n1. Update Phone Number\n2. Update Address\n3. Exit")
                chs = int(input("Enter your input:- "))
                if(chs == 1):
                    name = input("Enter Name:- ")
                    new_phoneno = input("Enter New Phone Number:- ")
                    qry = "UPDATE db_admission.tbl_admission SET stud_phoneno="+new_phoneno+" WHERE stud_name =" + "'" + name + "'"
                    cur.execute(qry)
                    con.commit()
                    con.close()
                    print("Mobile Number Updated...!")
                elif(chs == 2):
                    name = input("Enter Name:- ")
                    new_address = input("Enter New Address:- ")
                    qry = "UPDATE db_admission.tbl_admission SET stud_address=" + "'" + new_address + "'"+" WHERE stud_name =" + "'" + name + "'"
                    cur.execute(qry)
                    con.commit()
                    con.close()
                    print("Address Updated...!")
                elif(chs == 3):
                    break
                else:
                    print("Wrong Input...!")
                    
        elif(choice == 3):
            con = pymysql.connect(host = "localhost" , user = "root" , password = "root", database = "db_admission")
            cur = con.cursor()
            name = input("Enter Name:- ")
            qry = "DELETE from tbl_admission where stud_name=" + "'" + name + "'"
            cur.execute(qry)
            con.commit()
            con.close()
            print("Record Deleted...!")

        elif(choice == 4):
            con = pymysql.connect(host = "localhost" , user = "root" , password = "root", database = "db_admission")
            cur = con.cursor()
            while True:
                print("\n1. View All Admissions\n2. View Admissions by Class\n3. Exit")
                chos = int(input("Enter your Input:- "))
                if(chos == 1):
                    print("All Admission till Now...!")
                    qry = "SELECT * from tbl_admission"
                    cur.execute(qry)
                    rec = cur.fetchall()
                    for i in range(0 , len(rec)):
                        print(rec[i])
                    con.commit()
                    con.close()

                elif(chos == 2):
                    Class = input("Enter Class:- ")
                    print("Total Admissions of Class",Class,"is as follows:- ")
                    qry = "Select * from tbl_admission where stud_class =" + "'" + Class + "'"
                    print(qry)
                    cur.execute(qry)
                    rec = cur.fetchall()
                    for i in range(0 , len(rec)):
                        print(rec[i])
                    con.commit()
                                       

                elif(chos == 3):
                    break

                else:
                    print("Wrong input..!")

        elif(choice == 5):
            break
        
        else:
            print("Wrong Input...!")
    else:
        print("Wrong Password...! Try Again...!")
            
            
