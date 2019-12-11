def bubble_sort(arr):
    for i in range (len(arr)): 
        for j in range (len(arr)-1-i): 

        # if mylist[i] > mylist[i+1]:
            if arr[j] > arr[j+1]:

            # mylist[i],mylist[i+1]=mylist[i+1],mylist[i]
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
    return arr
arr1=[7,1,5,6,9,2]    
print(bubble_sort(arr1))
# arr1=[7,1,5,6,9,2] 
# print(mylist)/

