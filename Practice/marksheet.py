import json
n=int(input("Enter Total Number Of students: "))
d={}
for i in range(n):
    r=int(input("Enter Roll Number Of Students: "))
    name=input("Enter Name Of Students: ")
    maths=int(input("Enter Marks Of Maths: "))
    physics=int(input("Enter Marks Of Physics: "))
    chemistry=int(input("Enter Marks Of Chemistry: "))
    english=int(input("Enter Marks Of English: "))
    computer=int(input("Enter Marks Of Computer: "))
    total=maths+physics+chemistry+english+computer
    prcentage=(total/500)*100
    marks={'Maths':maths,'Physics':physics,'Chemistry':chemistry,'English':english,'Computer':computer,"Total":total,"Percentage":prcentage}
    d[r]={'Name':name,'Marks':marks}

c=int(input("Enter Roll Number Of Student: "))
print(json.dumps(d[c],indent=4)) 