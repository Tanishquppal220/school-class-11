import json
n=int(input("Enter Total Number Of students: "))
d={}


def fun():
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
             'English': english, 'Computer': computer, "Total": total, "Percentage": str(prcentage)+"%"}
    d[r] = {'Name': name, 'Marks': marks}
for i in range(n):
    fun()
    print()
    

index=0
while index!=4:
    print("1. Add Student Details")
    print("2. Display Student Details ")
    print("3. Student with More Than 75% Marks")
    print("4. Exit")
    index=int(input("Enter Your Choice: "))
    if index==1:
        fun()
        print()
    elif index==2:
        c=int(input("Enter Roll Number Of Student: "))
        print(json.dumps(d.get(c),indent=4), end="\n\n")
    elif index==3:
        for i in d:
            if d[i]['Marks']['Percentage']>'75%':
                Promoted=[]
                Promoted.append(d[i]['Name'])
        print(json.dumps(Promoted,indent=4),end="\n\n")
    else:
        print("Thank You")
        break 

