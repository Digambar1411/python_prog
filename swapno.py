

# using thord variabl

"""x=input("ente")
y=input("ente")
temp=0
temp=x
x=y
y=temp
print(x,y)"""

# without third vaibale
"""x=input("ente")
y=input("ente")
x,y = y,x
print(x,y)"""

#  using fumction

# Python Program to Swap Two Numbers

def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    # print("Befor swaping :x={} and y={}".format(n1,n2))
    print("After Swapping: x={} and y={}".format(a, b))
n1 = input(" Please Enter the First Value : ")
n2 = input(" Please Enter the Second Value : ")
swap_numbers(n1, n2)

