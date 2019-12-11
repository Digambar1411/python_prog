
# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    tall=max(ar)
    count=0
    for i in range(0,len(ar)):
        if(tall==ar[i]):
            count+=1
    print(count)     

if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

