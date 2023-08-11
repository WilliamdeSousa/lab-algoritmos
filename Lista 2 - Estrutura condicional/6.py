a = float(input())
b = float(input())
c = float(input())

if a == 0:
    print('NEESG')
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('NRR')
    else:
        print(f'{(-b + delta ** (1 / 2)) / (2 * a):.2f}')
        print(f'{(-b - delta ** (1 / 2)) / (2 * a):.2f}')