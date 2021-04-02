while True:
    print("1. View Available Glocery\n2. Add new item\n3. Update Item\n4. Exit")
    choice = int(input("Enter your choice:- "))
    if choice == 1:
        f = open("stock.txt","r")
        print(f.read())
        f.close()
        
    elif choice == 2:
        f = open("stock.txt","a")
        item = input("Enter new item:- ")
        qty = input("Enter its quantity:- ")
        f.write(item + "," + qty+"\n")
        f.close()
        
    elif choice == 3:
        f = open("stock.txt","r")
        data = f.read()
        f.close()
        grocery_stock = {}
        lines = data.split("\n")
        for line in lines:
            if("," in line):
                tempdata = line.split(",")
                grocery_stock[tempdata[0]] = int(tempdata[1])

        purchase_bag = {}
        n = int(input("How many Items you want to Update:- "))
        for i in range(n):
            item = input("Which Item you want to Update:- ")
            if item in grocery_stock.keys():
                qty = int(input("Enter quantity:- "))
                purchase_bag[item] = qty
                grocery_stock[item] = qty
        data = ""
        for item in grocery_stock:
            data += item + "," + str(grocery_stock[item]) + "\n"
        f = open("stock.txt","w")
        f.write(data)
        f.close
    else:
        break