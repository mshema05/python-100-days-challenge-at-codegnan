# get number of student in the class
n= inst(input("enter number of student in the class:"))
present+_count=0
absent_count=0
for roll no in range(1,n+1):
    status= input("enter", roll no, " is present  or absent and select following option 1 or 2\n 1.present \n 2. absent")

    #check status
    if status =='1':
        present_count+= 1
    elif status == '2':
        absent_count += 1
    else:
        print("print select either 1 or 2 options")
    print("total student in the class:",n)
    print("number of students present:",present_count)
    print(number of students absent:", absent_count)
    percentage =(present_count / n)* 100
    print("attendance report:", persentage)    
