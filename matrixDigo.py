n=int(input(":"))
arr=[]
for i in range(n):
    arr.append (list(map(int, input().rstrip().split())))
sum1=0
sum2=0
for i in range(n):
    for j in range(n):
        if (i==j):
           sum1+=arr[i][j] 
        if(i+j==n-1):
            sum2+=arr[i][j]
print(sum1) 
print(sum2) 
print(abs(res))

