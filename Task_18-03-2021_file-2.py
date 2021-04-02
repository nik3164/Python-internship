mobile = input("Enter your mobile number:- ")
while True:
    print("1. View Items\n2. Purchase Items\n3. Exit")
    ch = int(input("Enter Your choice:- "))
    if ch == 1:
        f = open("stock.txt","r")
        print(f.read())
        f.close()
    elif ch == 2:
        f2 = open("stock.txt","r")
        data = f2.read()
        f2.close()
 
        grocery_stock = {}
        lines = data.split("\n")
        for line in lines:
            if("," in line):
                tempdata = line.split(",")
                grocery_stock[tempdata[0]] = int(tempdata[1])

        purchase_bag = {}
        data = ""
        n = int(input("How many Items you want to purchase:- "))

        for i in range(n):
            item = input("Which Item you want to purchase:- ")
            if item in grocery_stock.keys():
                qty = input("Enter quantity:- ")
                if grocery_stock[item] > int(qty):
                    data += item + "," + qty + "\n"
                    grocery_stock[item] -= int(qty)
                else:
                    print("Required quantity is present in stock")
            else:
                print("Required item is not present in the stock")
        
        f = open(mobile+".txt","w")
        f.write(data)
        f.close()
        data = ""
        for item in grocery_stock:
            data += item + "," + str(grocery_stock[item]) + "\n"
        f = open("stock.txt","w")
        f.write(data)
        f.close
        f = open("stock.txt","r")
        print(f.read())     
    else:
        break
