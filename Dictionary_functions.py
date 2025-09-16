students={}
n=int(input("Enter the num of students:"))
for i in range(1,n+1):
    d={}
    d['roll']=int(input("Enter roll:"))
    d['name']=input("Enter name:")
    d['sem']=input("Enter sem:")
    students["stud"+str(i)] = d
print(students)

stud={}
count=0
choice=0
while True:
    flag=0
    print("1.Add\n 2.Search\n 3.Modify\n 4.Delete\n 5.Display\n 6.Exit")
    choice=int(input("Enter your choice"))
    if choice == 1:
        st={}
        st["usn"]=input("Enter USN:")
        st["name"]=input("Enter Name:")
        st["m1"]=int(input("Enter M1:"))
        st["m2"]=int(input("Enter M2:"))
        st["total"]=st["m1"]+st["m2"]
        st["per"]=st["total"]/2
        stud["stud"+str(count)]=st
        count=count+1
        del st
    elif choice==2:
        us=input("Enter usn to search:")
        for i in range(1,count):
            st=stud['stud'+str(i)]
            if st['usn']==us:
                print(st)
                flag=1
                break
            if flag==0:
                print("Record not found")
    elif choice==3:
        us=input("Enter usn to modify")
        for i in range(1,count):
            st=stud['stud'+str(i)]
            if st['usn']==us:
                st['name']=input("Enter new name:")
                st['m1']=int(input("Enter new m1:"))
                st['m2']=int(input("Enter new m2:"))
                st['total']=st['m1']+st['m2']
                st['per']=st['total']/2
                stud['stud'+str(i)]=st
                flag=1
                break
            if flag==0:
                print("Record not found")
    elif choice==4:
        us=input("Enter usn to delete:")
        for i in range(1,count):
            st=stud['stud'+str(i)]
            if st['usn']==us:
                del stud['stud'+str(i)]
                print("Student record deleted")
                count-=1
                flag=1
                break
        if flag==0:
            print("Record not found")
    elif choice==5:
        for i in range(1,count):
            print(stud['stud'+str(i)])
    elif choice==6:
        print("Thank you")
        break
    else:
        print("Invalid choice")
            

















    
                             
















                
            


        
