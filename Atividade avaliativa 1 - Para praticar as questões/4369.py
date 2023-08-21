a = int(input())
b = int(input())
c = int(input())
if a < 0 or b < 0 or c < 0:
    print('Restrição violada')
else:
    if a + b == c:
        print('+')
    else:
        print('-')