p = float(input())
d = int(input())
i = float(input())
a = str(input())
imp = mul = 0
crime = False
if i > p * 0.2:
    imp = 0.15 * i
if p > 1000000 and d < 0.9 * i:
    mul = 0.15 * i
if (p >= 1000000 and a == 'sim') or (p > 1000000 and i - d > 0.5 * p):
    crime = True
if crime:
    print('Crime')
elif imp == 0:
    print('Isento')
elif mul == 0:
    print('Imposto')
else:
    print('Imposto+Multa')
print(f'{imp:.1f}\n{mul:.1f}')