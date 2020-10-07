A=[0,1,2,3,4,5]
print(A)
temp=A[0]
for i in range(len(A)-1):
    A[i]=A[i+1]
A[len(A)-1]=temp
print(A)
temp=A[len(A)-1]
for i in range(len(A)-2,-1,-1):
    A[i+1]=A[i]
A[0]=temp
print(A)
N=19
B=[True]*N
B[0]=B[1]=False
for i in range (2,N):
    if B[i]:
        for j in range (2*i,N,i):
            B[j]=False
for i in range(N):
    print(i,'-',"simple" if B[i] else "complex")
