n = int(input())
tayoq = list(map(int, input().split()))

tayoq.sort()


for i in range(n - 1, 1, -1):  
    a, b, c = tayoq[i - 2], tayoq[i - 1], tayoq[i]
    if a + b > c:
        print(a, b, c)
        break
else:
    print(-1)