
num=int(input("enter a no:\n"))
# num1=int(input("enter a no:\n"))
if num>1:
    for i in range(2,num,100):
        if num%i==0:
            print("not prime")
            break
    else:
        print("prime") 
else:
    print("not prime")    
