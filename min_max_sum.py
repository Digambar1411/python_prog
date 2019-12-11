def miniMaxSum(arr):
    arr.sort()
    print(arr)
    min=0
    max=0
    for i in range(0,len(arr)-1):
        min+=arr[i]
    for i in range(1,len(arr)):
        max+=arr[i]    
    print(min,max)



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)