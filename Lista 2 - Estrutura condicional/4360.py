nota = float(input())
print(f'Nota digitada: {nota:.1f}')
if not (0 <= nota <= 10):
    print('A nota nao esta no intervalo [0,10]')