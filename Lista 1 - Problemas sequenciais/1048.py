salario = float(input())
horas_extras = int(input())
salario_por_hora = (salario / 44) * 1.1
salario_final = salario + horas_extras * salario_por_hora
print(f'{salario_final:.2f}')
