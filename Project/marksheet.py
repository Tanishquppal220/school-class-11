import json
n = eval(input("Enter Total Number Of students: "))
# d = {1: {'Name': 'Tanishq', 'Marks': {'Maths': 98, 'Physics': 97, 'Chemistry': 95, 'English': 93, 'Computer': 100, 'Total': 483, 'Percentage': 96}},2: {'Name': 'Hardik', 'Marks': {'Maths': 92, 'Physics': 93, 'Chemistry': 95, 'English': 94, 'Computer': 100, 'Total': 474, 'Percentage': 94}}}
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
while index != 4:
    print("1. Add Student Details")
    print("2. Display Student Details ")
    print("3. Student with More Than 75% Marks")
    print("4. Delete Student Details")
    print("5. Exit")
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
        marks = {'Maths': maths, 'Physics': physics, 'Chemistry': chemistry,'English': english, 'Computer': computer, "Total": total, "Percentage": prcentage}
        d[r] = {'Name': name, 'Marks': marks}
        print()
    elif index == 2:
        c = int(input("Enter Roll Number Of Student: "))
        print(json.dumps(d.get(c), indent=4), end="\n\n")
    elif index == 3:
        g = {}
        l = []
        for i in d:
            g[d[i]['Name']] = d[i]['Marks']['Percentage']
        for j in g:
            if g[j] > 75:
                l.append(j)
        print(json.dumps(l, indent=4), end="\n\n")
    elif index == 4:
        c = int(input("Enter Roll Number Of Student: "))
        confirm = input(
            "Are You Sure You Want To Delete This Student Details (Y/N): ")
        if confirm == 'Y':
            d.pop(c)
            print("Student Details Deleted Successfully")
        else:
            continue
    else:
        print("Thank You")
        break
print(d.keys())
