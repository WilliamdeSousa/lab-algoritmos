num = float(input())
soma = cont = 0
while num != -1:
    soma += num
    cont += 1
    num = float(input())
print(f'{soma / cont:.2f}')