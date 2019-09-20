'''
lst2=[]
n = int(input())
arr = map(int, input().split())
lst1=list(arr)
print(lst1)
lst1.sort(reverse=True)
print("after sort :",lst1)
for i in range (len(lst1)):
    if lst1[i] not in lst2:
        lst2.append(lst1[i])
print("after append :",lst2)
# print(lst2)     
print(lst2[1])
'''
if __name__ == '__main__':
    lst1=[]
    n = int(input("Enter no of values:"))
    arr = map(int, input().split())
    lst=list(arr)
    lst.sort(reverse=True)
    for i in range (len(lst)):
        if lst[i] not in lst1:
            lst1.append(lst[i])
    print(lst1[1])          
    # return runner value from array
