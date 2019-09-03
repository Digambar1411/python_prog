num=int(input("ente a 1st no:"))
num1=int(input("ente a 2nd no:"))
for i in range(num,num1):
    if i>1:
        for p in range(2,i):
           if i%p==0:
                break
        else:
            print(i)        