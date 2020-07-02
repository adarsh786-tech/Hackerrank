def plusMinus(arr, n):
    pos=0
    neg=0
    zero=0

    for i in range(n):
        if(arr[i] <0):
            neg+=1
        elif(arr[i] >0):
            pos+=1
        else:
            zero+=1
    print(pos/n)
    print(neg/n)
    print(zero/n)

if __name__ == '__main__':
    n=int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr,n)
