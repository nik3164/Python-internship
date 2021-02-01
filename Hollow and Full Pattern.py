n = 11
print("Rectangle")
for i in range(5):
    for j in range(7):
        print("* ",end = "")
    print()

print("Hollow Rectangle")
for i in range(5):
    for j in range(7):
         if(i == 0 or i == 5 - 1 or j == 0 or j == 7 - 1):
            print("* ",end = "")
         else:
            print("  ",end = "")
    print()
    

for i in range(80):
    print("-",end='')
print()

print("Diamond")
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end = "")
    for j in range(1,2*i):
        print("*",end = "")
    print()
for i in range(n-1,0,-1):
    for j in range(1,n-i+1):
        print(" ",end = "")
    for j in range(1,2*i):
        print("*",end = "")
    print()

print("Hollow Diamond.....!")
for i in range(1, n+1):
    for j in range(1,n-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(n-1,0, -1):
    for j in range(1,n-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(80):
    print("-",end="")
print()

print("Left Vertical Tringle .....!")
mid=int(n/2)
for i in range(n):
    if(i<=mid):
        for j in range(mid-i):
            print("  ",end="")
        for k in range(i+1):
            print("* ",end="")
    else:
        for j in range(i-mid):
            print("  ",end="")
        for k in range(n-i):
            print("* ",end="")
    print()


print("Hollow Left Vertical Tringle .....!")
mid=int(n/2)
for i in range(n):
    if(i<=mid):
        for j in range(mid-i):
            print("  ",end="")
        for k in range(i+1):
            if(k==0 or k==i):
                print("* ",end="")
            else:
                print("  ",end="")
    else:
        for j in range(i-mid):
            print("  ",end="")
        for k in range(n-i):
            if(k==n-i-1 or k==0):
                print("* ",end="")
            else:
                print("  ",end="")
    print()


for i in range(80):
    print("-",end="")
print()

print("Right Angled tringle")

for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print()


print("Hollow Right Angled tringle")

for i in range(n):
    for j in range(i+1):
        if j==0 or j==i or i==n-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

for i in range(80):
    print("-",end="")
print()

print("Square")
for i in range(n):
    for j in range(n):
        print("* ",end = "")
    print()

print("Hollow Square")
for i in range(n):
    for j in range(n):
        if(i == 0 or i == n-1 or j == 0 or j == n-1):
            print("* ",end = "")
        else:
            print("  ",end = "")
    print()

for i in range(80):
    print("-",end="")
print()

print("Left Angled tringle")
for i in range(n):
    for s in range(n, i+1, -1):
        print("  ", end="")
    for j in range(i+1):
            print("* ", end="")
    print()


print("Hollow Left Angled tringle")
for i in range(n):
    for s in range(n, i+1, -1):
        print("  ", end="")
    for j in range(i+1):
        if j == 0 or j == i or i == n-1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

for i in range(80):
    print("-",end="")
print()

print("Inverted Left Angled Tringle")
for i in range(n):
        for s in range(i):
            print("  ",end="")
        for j in range(i, n):
            print("* ",end="")
        print()


print("Hollow Inverted Left Angled Tringle")
for i in range(n):
        for s in range(i):
            print("  ",end="")
        for j in range(i, n):
            if(i == 0 or j == i or j == n-1):
                print("* ",end="")
            else:
                print("  ",end="")
        print()

for i in range(80):
    print("-",end="")
print()

print("Equilateral tringle")
for i in range(n):
    for s in range(n, i+1, -1):
        print(" ", end="")
    for j in range(i+1):
        #if j == 0 or j == i or j == n+1:
            print("* ", end="")
        #else:
            #print(" ", end="")
    print()

print("Hollow Equilateral tringle")
for i in range(n):
    for s in range(n, i+1, -1):
        print(" ", end="")
    for j in range(i+1):
        if j == 0 or j == i or i == n-1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

for i in range(80):
    print("-",end="")
print()

print("Inverted Equilateral Tringle")
for i in range(n):
        for s in range(i):
            print(" ",end="")
        for j in range(i, n):
            print("* ",end="")
        print()

print("Inverted Equilateral Tringle")
for i in range(n):
        for s in range(i):
            print(" ",end="")
        for j in range(i, n):
            if(j ==0 or j == i or j == n-1):
                print("* ",end="")
            else:
                print("  ",end="")
        print()

for i in range(80):
    print("-",end="")
print()

print("Inverted Right Angled Tringle")
for i in range(n-1,-1,-1):
    for j in range(i+1):
        print("*",end="")
    print(" ")


print("Hollow Inverted Right Angled Tringle")
for i in range(n-1,-1,-1):
    for j in range(i+1):
        if(j ==0 or j == i or i == n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range(80):
    print("-",end='')
print()

print("Right Vertical Tringle")
mid=int(n/2)
for i in range(n):
    if(i<=mid):
        for j in range(i+1):
            print("* ",end="")
    else:
        for j in range(n-i):
            print("* ",end="")
    print()

print("Hollow Right Vertical Tringle")
mid=int(n/2)
for i in range(n):
    if(i<=mid):
        for j in range(i+1):
            if(i == j or j == 0):
                print("* ",end="")
            else:
                print(" ",end = "")
    else:
        for j in range(n-i):
            if(i == j or j == 0 or j == n - i - 1):
                print("* ",end="")
            else:
                print(" ",end = "")
    print()
