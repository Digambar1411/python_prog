

# Complete the hackerrankInString function below.
# def hackerrankInString(s):
h="hackerrank"
h=list(h)
s="afEWHRERBVHEREBQTRNJAHSDFWAD"
s1=list(s)

print(s1)
for i in range(0,len(h)):
    if h[i] not in s1:
        break
    else:
        print("yes")        

    #             print("No")
    #         else:
    #             print("Yes")    

# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input())

#     for q_itr in range(q):
#         s = input()

#     result = hackerrankInString(s)

    #     fptr.write(result + '\n')

    # fptr.close()
