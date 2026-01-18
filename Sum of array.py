
A=[]
Sum = 0
n= int(input("Enter a array lenght"))
for i in range(n):
    A.append(int(input("Enter a number")))#insert needs 2 values
    # append can work with one value
    Sum=Sum+A[i]

print("Sum of numbers:", Sum)
