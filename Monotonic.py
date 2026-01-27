A=[]
n=int(input("Enter a length of a array"))
for i in range(n):
    A.append(int(input("Enter a number:")))

incr = all(A[i] <= A[i+1] for i in range(n-1))
decr = all(A[i] >= A[i+1] for i in range(n-1))

print(incr or decr)
