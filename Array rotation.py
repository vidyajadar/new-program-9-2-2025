A=[]
n=int(input("Enter the length of the array"))

for i in range(n):
    A.append(int(input("Enter a number")))

B=[]
for i in range (n, 0,-1):
    B.append(i)

print(B)

# d=2
# n=len(A)
# A.reverse()
# A[:n-d] = A[:n-d][::-1]
# A[n-d:] = A[n-d:][::-1]
# print(A)


