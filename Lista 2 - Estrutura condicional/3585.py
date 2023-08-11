tipo = str(input())
n1 = float(input())
n2 = float(input())
n3 = float(input())
notas_erradas = caracter_errado = False
if tipo != 'a' and tipo != 'p' and tipo != 'h':
    print('Caractere invalido')
else:
    if n1 > 10 or n2 > 10 or n3 > 10:
        print('Notas erradas')
    else:
        if tipo == 'a':
            m = (n1 + n2 + n3) / 3
            print(f'{m:.2f}')
        elif tipo == 'p':
            p1 = float(input())
            p2 = float(input())
            p3 = float(input())
            m = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3)
            print(f'{m:.2f}')
        elif tipo == 'h':
            m = 3 / ((1 / n1) + (1 / n2) + (1 / n3))
            print(f'{m:.2f}')
        if m >= 7:
            print('Aprovado')
        elif m <= 4:
            print('Reprovado')
        else:
            print('Prova final')