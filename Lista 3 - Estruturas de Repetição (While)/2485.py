voto = int(input())
v4 = v5 = v9 = 0
while voto != 0:
    if voto == 4:
        v4 += 1
    elif voto == 5:
        v5 += 1
    elif voto == 9:
        v9 += 1
    voto = int(input())
if v4 > v5 and v4 > v9:
    print(f'canal 4: {v4}')
    if v5 > v9:
        print(f'canal 5: {v5}')
        print(f'canal 9: {v9}')
    else:
        print(f'canal 9: {v9}')
        print(f'canal 5: {v5}')
elif v5 > v4 and v5 > v9:
    print(f'canal 5: {v5}')
    if v4 > v9:
        print(f'canal 4: {v4}')
        print(f'canal 9: {v9}')
    else:
        print(f'canal 9: {v9}')
        print(f'canal 4: {v4}')
else:
    print(f'canal 9: {v9}')
    if v5 > v4:
        print(f'canal 5: {v5}')
        print(f'canal 4: {v4}')
    else:
        print(f'canal 4: {v4}')
        print(f'canal 5: {v5}')
