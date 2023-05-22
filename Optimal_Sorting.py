n = int(input())
for i in range(n):
    x = int(input())
    a = list(map(int, input().split()))
    c = 0
    for j in range(x-1):
        if a[j] <= a[j+1]:
            c += 1
    if c+1 == x:
        print(0)
    else:
        b = max(a)
        h = min(a)
        print(b-h)