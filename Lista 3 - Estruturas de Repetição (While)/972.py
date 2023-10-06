n = int(input())
while n != -1:
    nd = 0
    for i in range(1, n + 1, 1):
        if n % i == 0:
            nd += 1
    if nd == 2:
        print(1)
    else:
        print(0)
    n = int(input())