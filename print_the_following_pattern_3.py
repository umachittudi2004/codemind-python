n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if j==0:
            print('*',end=' ')
        elif j==n-1:
            print('*',end=' ')
        elif(i==j):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()