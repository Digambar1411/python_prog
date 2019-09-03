num = input('Enter any number/string : ')
r=num[::-1]
if num==r:
    print("reverse:",r)
    print('The given number is PALINDROME')
else:
    print('The given number is  not PALINDROME') 