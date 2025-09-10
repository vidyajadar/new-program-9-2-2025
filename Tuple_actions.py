l=[]
n=int(input("Enter the size of stack"))
i=1
while i<=n:
    choice=print("1.push\n2.pop\n3.display\n4.exit")
    if choice == 1:
        a=int(input("Enter a element to be pushed"))
        if top == n-1:
            print("Stack is overflow")
        else:
            for top in range(0,n):
                l.insert(i,l[i])
    elif choice == 2:
        b=int(input("Enter a element to be pop"))
        if top == -1:
            print("stack is underflow")
        else:
            for top in range(n-1,-1,-1):
                l.pop(l[i])
    elif choice == 3:
        for i in range(n-1,0,1):
            l.append(int(input("Enter a number")))
    else:
        break
    
