'''
f = open("File.txt",'a')
print("File Opened...!")
f.write("Ok B Bye!")
f.close()
f = open("File.txt",'r')
print(f.read())
f.close()
print("file Closed...!")

'''
info = ""
name = input("Enter your Name:- ")


file = open("Stud_info.txt",'w')
file.write(name)
file.close()
f = open("Stud_info.txt",'r')
print(f.read())
f.close()
