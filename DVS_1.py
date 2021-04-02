import matplotlib.pyplot as plt
d = {}
with open("sampledata.txt") as f:
    for line in f:
        (key, val) = line.split(",")
        d[str(key)] = int(val)
print(d)
plt.xlabel("Items")
plt.ylabel("Stocks Available")
plt.bar(d.keys(), d.values())
plt.show()
plt.plot(d.keys(), d.values())
plt.show()
#plt.hist(d.keys(), d.values(), bins=25)
#plt.show()
plt.scatter(d.keys(), d.values())
plt.show()
plt.plot(d.keys(), d.values())
plt.grid()
plt.show()
plt.plot(d.keys(), d.values(), marker = '*')
plt.grid()
plt.show()