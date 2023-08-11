l = float(input())
t = str(input())
if t == 'A':
    if l <= 20:
        d = 0.97
    else:
        d = 0.95
    v = l * d * 1.9
elif t == 'G':
    if l <= 20:
        d = 0.96
    else:
        d = 0.94
    v = l * d * 2.5
elif t == 'D':
    if l <= 25:
        d = 1
    else:
        d = 0.96
    v = l * d * 1.66
print(f'R$ {v:.2f}')