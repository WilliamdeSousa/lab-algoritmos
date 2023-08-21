l, r, d = [int(i) for i in input().split()]
if not 0 <= l <= 100 or not 0 <= l <= 100 or not 0 <= l <= 100:
    print('Violação das restrições')
else:
    if (r > 50) and (l < r) and (r > d):
        print('S')
    else:
        print('N')