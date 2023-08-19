n_casos = int(input())
for i in range(n_casos):
    v1, v2, d1, d2 = [int(i) for i in input().split()]
    while v1 > 0 and v2 > 0:
        qr_clodes = (v2 // d1 + 1) if v2 % d1 != 0 else (v2 // d1)
        qr_bezaliel = (v1 // d2 + 1) if v1 % d2 != 0 else (v1 // d2)
        if qr_bezaliel < qr_clodes:
            d1 += 50
        else:
            v2 -= d1
        if v2 > 0:
            v1 -= d2
    if v1 <= 0:
        print('Bezaliel')
    else:
        print('Clodes')
