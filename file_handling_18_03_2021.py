f = open("Files.txt",'r')
data = f.read()
print(data)
f.close()
stocks = {}
lines = data.split('\n')
for line in lines:
    if("," in line):
        tempdata = line.split(",")        
        stocks[tempdata[0]] = int(tempdata[1])
print(stocks)
stocks_bag = {}
data = " "
n = int(input("How many items you want to purchase ?"))
for i in range(n):
    item = input("Enter item name: -")
    if(item in stocks.keys()):
        quantity = int(input("Enter how many quantity you want of "+item+": -"))
        if stocks[item]> quantity:
            stocks_bag[item] = quantity
            stocks[item] -=quantity
print(stocks_bag)
print(stocks)

