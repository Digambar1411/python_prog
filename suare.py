
 # for i in range(2,9+1):
 #     if i%2!=0:
 #         print(i)


def print_full_name(a, b):
    print(f'Hello {a} {b}! You just delved into python.')

if __name__ == '__main__':
    f = input("Enter first name:")
    l = input("Enter last name:")
    if len(f)==0 or len(l)==0 :
        print("name cannot be null")     
        break 
    # if len(f)<=10:
    #     if len(l)<=10:
    #         print_full_name(f, l)
    # else:
    #     print("length of first nameshould be less than 10")  
    