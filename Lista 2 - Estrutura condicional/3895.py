salario = float(input())
valor_fixo = float(input())
preco_km = float(input())
km_pecorridos = float(input())
fim_semana = 1.1 if int(input()) == 1 else 1

tarifa = (valor_fixo + preco_km * km_pecorridos) * fim_semana

resultado = salario * 0.3 - tarifa
if resultado < 0:
    print(f'Não vai poder viajar.\n{resultado * -1:.2f}')
else:
    print(f'Vai poder viajar.\n{tarifa:.2f}\n{resultado:.2f}')