
if __name__ == '__main__':
    n = int(input("enter no of number to be enter:"))

    arr = list(map(int, input().rstrip().split()))
    l=list(arr)
    for i in reversed(range(0,len(l))):
        print(l[i],end=" ")        