d1 = int(input())
d2 = int(input())
m = int(input())
f = (10 * m) / (d1 + d2)
print(f'Scar conseguiu criar uma frustração {f:.2f} na turma')
if f >= 4:
    print('Eu matei Mufasa')
elif f > 2:
    print('Consegui lacaios preciosos')
else:
    print('Mais um fracasso...')