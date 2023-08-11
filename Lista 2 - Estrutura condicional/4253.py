figura = str(input())
if figura == 'retangulo':
    base = float(input())
    altura = float(input())
    print(f'{base * altura:.2f}')
elif figura == 'triangulo':
    base = float(input())
    altura = float(input())
    print(f'{(base * altura) / 2:.2f}')
elif figura == 'trapezio':
    basemaior = float(input())
    basemenor = float(input())
    altura = float(input())
    print(f'{((basemaior + basemenor) * altura) / 2:.2f}')
elif figura == 'circulo':
    raio = float(input())
    print(f'{(raio ** 2) * 3.1415:.2f}')
else:
    print('Figura invalida.')