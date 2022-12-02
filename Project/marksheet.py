import json
n = eval(input("Enter Total Number Of students: "))
d = {}
for k in range(n):
    r = int(input("Enter Roll Number Of Students: "))
    name = input("Enter Name Of Students: ")
    maths = int(input("Enter Marks Of Maths: "))
    physics = int(input("Enter Marks Of Physics: "))
    chemistry = int(input("Enter Marks Of Chemistry: "))
    english = int(input("Enter Marks Of English: "))
    computer = int(input("Enter Marks Of Computer: "))
    total = maths+physics+chemistry+english+computer
    prcentage = int((total/500)*100)
    marks = {'Maths': maths, 'Physics': physics, 'Chemistry': chemistry,
             'English': english, 'Computer': computer, "Total": total, "Percentage": prcentage}
    d[r] = {'Name': name, 'Marks': marks}
    print()

index = 0

while index != 6:
    print("1. Add Student Details")
    print("2. Display Student Details ")
    print("3. Student with More Than 75% Marks")
    print("4. Delete Student Details")
    print("5. Print Whole dict")
    print("6. Exit")
    index = int(input("Enter Your Choice: "))
    print()
    if index == 1:
        r = int(input("Enter Roll Number Of Students: "))
        name = input("Enter Name Of Students: ")
        maths = int(input("Enter Marks Of Maths: "))
        physics = int(input("Enter Marks Of Physics: "))
        chemistry = int(input("Enter Marks Of Chemistry: "))
        english = int(input("Enter Marks Of English: "))
        computer = int(input("Enter Marks Of Computer: "))
        total = maths+physics+chemistry+english+computer
        prcentage = int((total/500)*100)
        marks = {'Maths': maths, 'Physics': physics, 'Chemistry': chemistry,
                 'English': english, 'Computer': computer, "Total": total, "Percentage": prcentage}
        d[r] = {'Name': name, 'Marks': marks}
        print()
    elif index == 2:
        c = int(input("Enter Roll Number Of Student: "))
        g = d[c]['Marks']
        print("Roll Number Of Student:", c)
        print("Name Of Student:", d[c]['Name'])
        print("Marks Of Student is:")
        for i in g:
            for i in ['Total', 'Percentage']:
                print("\t", end="")
                a = i+""+":"+""+str(g[i])
                print("Marks Of ", i, "are", ":", g[i])
        print("Total Marks Of Student is:", g['Total'])
        print("Percentage Of Student is:", g['Percentage'])
    elif index == 3:
        g = {}
        l = []
        for i in d:
            g[d[i]['Name']] = d[i]['Marks']['Percentage']
        for j in g:
            if g[j] > 75:
                l.append(j)
        for i in l:
            a = i
            print(a)
    elif index == 4:
        c = int(input("Enter Roll Number Of Student: "))
        if c in d:
            confirm = input(
                "Are You Sure You Want To Delete This Student Details (Y/N): ")
            if confirm in ['Y', 'y']:
                print(json.dumps(d[c], indent=4), end="\n\n")
                d.pop(c)
                print("Deleted Successfully")
            else:
                continue
        else:
            print(c, "Not in The list")
    elif index == 5:
        print(json.dumps(d, indent=4), end="\n\n")
    else:
        print("Thank You")
        break
