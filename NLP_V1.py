while True:
    print("\n1. Number of words\n2. Number of Characters\n3. Number of Lines\n4. Number of Sentences\n5. Exit\n")
    choice = int(input("Enter your choice: - "))
    if choice == 1:
        f = open("data.txt", 'r')
        lines = f.read().split()
        f.close()
        print(lines)
        print("Number of Words in file is :- ", len(lines))



    elif choice == 2:
        f = open("data.txt", 'r')
        lines = f.read().replace(" ", "")
        f.close()
        print("Number of Characters in file is :- ", len(lines), "(Without white spaces)")
        f = open("data.txt", 'r')
        lines_with_space = f.read()
        f.close()
        print("Number of Characters in file is :- ", len(lines_with_space), "(With white spaces)")

    elif choice == 3:
        f = open("data.txt", 'r')
        lines = f.read().split("\n")
        f.close()
        print("Number of lines in file is :- ", len(lines))

    elif choice == 4:
        f = open("data.txt", 'r')
        lines = f.read().split(".")
        f.close()
        print("Number of Sentences in file is :- ", len(lines))

    elif choice == 5:
        exit()

    else:
        print("Enter valid Input...!")