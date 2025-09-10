l=[]
front=0
size=int(input("Enter size of a list"))
last=size-1
for i in range(size):
    a=int(input("Enter the data:"))
    l.append(a)

while True:
    print("1.Insert front\n 2.Insert last\n 3.Delete first\n 4.Delete last\n 5.Delete specified position\n 6.Insert in specified position\n 7.Display\n 8.Exit")
    choice = int(input("Enter your choice"))
    if choice == 1:
        d=int(input("Enter the element to be added"))
        l.insert(0,d)
    elif choice == 2:
        d=int(input("Enter the element to be added at last"))
        l.insert(-1,d)
    elif choice ==3:
        l.remove(l[0])
    elif choice == 4:
        l.pop()
    elif choice ==5:
        s=int(input("Enter the position to be deleted:"))
        l.remove(l[s])
    elif choice == 6:
        s=int(input("Enter the position to be inserted:"))
        l.insert(l[s])
    elif choice == 7:
        print(l)
    elif choice == 8:
        break
    else:
        print("Invalid Entry")

        
