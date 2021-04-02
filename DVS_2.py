import pymysql
import matplotlib.pyplot as plt
con = pymysql.connect(host="localhost", user="root", password="root", database="db_student")
cur = con.cursor()
qry = "Select stud_name , stud_marks from tbl_student"
cur.execute(qry)
info = cur.fetchall()
#for i in range(0, len(info)):
#    print(info[i])
con.commit()
con.close()

data = {}
data2 = {}
data3 = {}
passed , failed = 0, 0
for line in info:
    key , value = line
    data[str(key)] = int(value)
    if value > '40':
        data2[str(key)] = int(value)
        passed = passed + 1
    else:
        data3[str(key)] = int(value)
        failed = failed + 1
print("data is printed------------>\n",data)

print(passed , failed)
plt.bar("Passed", passed)
plt.bar("Failed", failed)
plt.show()