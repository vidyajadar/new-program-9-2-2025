def read(l,n):
    for i in range(n):
        a=int(input("Enter a num:"))
        l.append(a)

def display(l,n):
    for x in l:
        print(x)

l=[]
n=int(input("Enter size of a list:"))
read(l,n)
display(l,n)
