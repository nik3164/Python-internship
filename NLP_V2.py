while True:
    print("\n1. Number of words\n2. Number of Characters\n3. Number of Lines\n4. Number of Sentences\n5. Exit\n")
    choice = int(input("Enter your choice: - "))
    if choice == 1:
        list1 = []
        f = open("data2.txt", 'r')
        lines = f.read().split()
        f.close()
        print("Number of Words in file before removing stopwords is :- ", len(lines))
        f2 = open("stopwords.txt", 'r')
        f2_lines = f2.read()
        f2.close()
        for line in lines:
            if line not in f2_lines:
                list1.append(line)
        print("Number of Words in file after removing stopwords is :- ", len(list1))

    elif choice == 2:
        list2 = []
        list3 = []
        f = open("data.txt", 'r')
        lines = f.read().replace(" ", "")
        f.close()
        print("Number of Characters in file before removing stopwords is :- ", len(lines), "(Without white spaces)")
        f2 = open("stopwords.txt", 'r')
        f2_lines = f2.read()
        f2.close()
        for line in lines:
            if line not in f2_lines:
                list2.append(line)
        print("Number of Characters in file after removing stopwords is:- ",len(list2),"(Without white spaces)")

        f = open("data.txt", 'r')
        lines_with_space = f.read()
        f.close()
        print("\nNumber of Characters in file before removing stopwords is :- ", len(lines_with_space), "(With white spaces)")
        f2 = open("stopwords.txt", 'r')
        f2_lines = f2.read()
        f2.close()
        for line in lines:
            if line not in f2_lines:
                list3.append(line)
        print("Number of Characters in file after removing stopwords is:- ", len(list3), "(With white spaces)")

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
