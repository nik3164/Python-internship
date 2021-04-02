try:
    import pymysql
    import datetime
except Exception as e:
    print("Importing not done...!\n", e)
else:
    con = pymysql.connect(host="localhost", user="root", password="root", database="db_engineering")
    cur = con.cursor()

    who = input(" Admin or Student?")
    password = input("Enter Password:- ")
    flag = False
    qry1 = "SELECT password FROM tbl_login WHERE password=" + "'" + password + "'"
    try:
        cur.execute(qry1)
    except Exception as e:
        print("Query not executed...!\n", e)
    else:
        Password = cur.fetchall()
        if len(Password) >= 1:
            flag = True
        else:
            flag = False
        con.commit()
        con.close()

    while True:
        if flag:
            data = "\n1. New Admission\n2. Update Info\n3. Remove Admission\n4. View Admissions\n5. Exit\n"
            print(data)
            choice = int(input("Enter your Choice:- "))
            if who == 'admin':
                file = open("AdminLog.txt", 'a')
                file.write("\n" + str(choice) + " , ")
                file.close()
            else:
                file = open("StudentLog.txt", 'a')
                file.write("\n" + str(choice) + " , ")
                file.close()

            if choice == 1:
                con = pymysql.connect(host="localhost", user="root", password="root", database="db_engineering")
                cur = con.cursor()
                name = input("Enter Name:- ")
                Class = input("Enter Class:- ")
                div = input("Enter Division:- ")
                phoneno = input("Enter Mobile Number:- ")
                address = input("Enter Address:- ")
                Name = name
                qry = "INSERT into db_engineering.tbl_admission values (0,'" + name + "','" + Class + "','" + div + \
                      "','" + phoneno + "','" + address + "')"
                cur.execute(qry)
                con.commit()
                con.close()
                print("Record Added...!")

                if who == 'admin':
                    f = open("AdminLog.txt", 'a')
                    f.write(" New User Registered. , " + str(datetime.datetime.now()))
                    f.close()
                elif who == 'student':
                    f = open("StudentLog.txt", 'a')
                    f.write(" New User Registered. , " + str(
                        datetime.datetime.now()) + " , New User " + name + " Registered.")
                    f.close()

            elif choice == 2:
                con = pymysql.connect(host="localhost", user="root", password="root", database="db_engineering")
                cur = con.cursor()
                while True:
                    print("\n1. Update Phone Number\n2. Update Address\n3. Exit")
                    chs = int(input("Enter your input:- "))
                    if chs == 1:
                        name = input("Enter Name:- ")
                        new_phoneno = input("Enter New Phone Number:- ")
                        Name = name
                        qry = "UPDATE db_engineering.tbl_admission SET stud_phoneno=" + new_phoneno + \
                              " WHERE stud_name =" + "'" + name + "'"
                        cur.execute(qry)
                        con.commit()
                        con.close()
                        print("Mobile Number Updated...!")
                        if who == 'admin':
                            f = open("AdminLog.txt", 'a')
                            f.write("phone number Updated. ," + str(datetime.datetime.now()))
                            f.close()
                        elif who == 'student':
                            f = open("StudentLog.txt", 'a')
                            f.write("phone number Updated. ," + str(
                                datetime.datetime.now()) + " , User " + name + "'s Phone number updated.")
                            f.close()

                    elif chs == 2:
                        name = input("Enter Name:- ")
                        new_address = input("Enter New Address:- ")
                        Name = name
                        qry = "UPDATE db_engineering.tbl_admission SET stud_address=" + "'" + new_address + "'" + \
                              " WHERE stud_name =" + "'" + name + "'"
                        cur.execute(qry)
                        con.commit()
                        con.close()
                        print("Address Updated...!")
                        if who == 'admin':
                            f = open("AdminLog.txt", 'a')
                            f.write(" Address Updated. ," + str(datetime.datetime.now()))
                            f.close()
                        elif who == 'student':
                            f = open("Student.txt", 'a')
                            f.write(" Address Updated. , " + str(
                                datetime.datetime.now()) + " , User " + name + "'s Address updated. ")
                            f.close()

                    elif chs == 3:
                        break
                    else:
                        print("Wrong Input...!")

            elif choice == 3:
                con = pymysql.connect(host="localhost", user="root", password="root", database="db_engineering")
                cur = con.cursor()
                name = input("Enter Name:- ")
                Name = name
                qry = "DELETE from tbl_admission where stud_name=" + "'" + name + "'"
                cur.execute(qry)
                con.commit()
                con.close()
                print("Record Deleted...!")
                if who == 'admin':
                    f = open("AdminLog.txt", 'a')
                    f.write(" User Removed. ," + str(datetime.datetime.now()))
                    f.close()
                elif who == 'student':
                    f = open("StudentLog.txt", 'a')
                    f.write(" User Removed. , " + str(datetime.datetime.now()) + " , User " + name + " Removed. ")
                    f.close()

            elif choice == 4:
                con = pymysql.connect(host="localhost", user="root", password="root", database="db_engineering")
                cur = con.cursor()
                while True:
                    print("\n1. View All Admissions\n2. View Admissions by Class\n3. Exit")
                    chos = int(input("Enter your Input:- "))
                    if chos == 1:
                        con = pymysql.connect(host="localhost", user="root", password="root", database="db_engineering")
                        cur = con.cursor()
                        print("All Admission till Now...!")
                        qry = "SELECT * from tbl_admission"
                        cur.execute(qry)
                        rec = cur.fetchall()
                        for i in range(0, len(rec)):
                            print(rec[i])
                        con.commit()
                        con.close()
                        if who == 'admin':
                            f = open("AdminLog.txt", 'a')
                            f.write(" All Admitted students data displayed. ," + str(datetime.datetime.now()))
                            f.close()
                        elif who == 'student':
                            f = open("StudentLog.txt", 'a')
                            f.write(" All Admitted students data displayed. , " + str(
                                datetime.datetime.now()) + " , All data displayed. ")
                            f.close()

                    elif chos == 2:
                        con = pymysql.connect(host="localhost", user="root", password="root", database="db_engineering")
                        cur = con.cursor()
                        Class = input("Enter Class:- ")
                        print("Total Admissions of Class", Class, "is as follows:- ")
                        qry = "Select * from tbl_admission where stud_class =" + "'" + Class + "'"
                        print(qry)
                        cur.execute(qry)
                        rec = cur.fetchall()
                        for i in range(0, len(rec)):
                            print(rec[i])
                        con.commit()
                        if who == 'admin':
                            f = open("AdminLog.txt", 'a')
                            f.write(" All Admitted students data displayed catagarised by Class " + Class + ". ," + str(
                                datetime.datetime.now()))
                            f.close()
                        elif who == 'student':
                            f = open("StudentLog.txt", 'a')
                            f.write(
                                " All Admitted students data displayed catagarised by Class " + Class + ". , " + str(
                                    datetime.datetime.now()) + " , All data displayed ordered by Class. ")
                            f.close()

                    elif chos == 3:
                        break

                    else:
                        print("Wrong input..!")

            elif choice == 5:
                if who == 'admin':
                    f = open("AdminLog.txt", 'a')
                    f.write(" User Exited. ," + str(datetime.datetime.now()))
                    f.close()
                elif who == 'student':
                    f = open("StudentLog.txt", 'a')
                    f.write(" Exited. ," + str(datetime.datetime.now()) + " , User Exited. ")
                    f.close()
                break

            else:
                print("Wrong Input...!")
        else:
            print("Wrong Password...!")
            break
