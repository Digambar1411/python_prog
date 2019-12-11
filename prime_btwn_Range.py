# num=int(input("ente a 1st no:"))
# num1=int(input("ente a 2nd no:"))
# for i in range(num,num1):
#     if i>1:
#         for p in range(2,i):
#            if i%p==0:
#                 break
#         else:
#             print(i,end=" ")        

def prime_check(a,b):
    for i in range(a,b):
        if i>1:
            for p in range(2,i):
                if i%p==0:
                    break
            else:
                print(i,end=" ")

n1=int(input("enter a 1st no:"))
n2=int(input("enter a 2nd no:")) 
prime_check(n1,n2)                           