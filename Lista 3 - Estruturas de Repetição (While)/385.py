matricula = str(input())
cre = float(input())
pior, menor_cre = matricula, cre
soma = cre
cont = 1
while matricula != '999':
    if cre < menor_cre:
        pior, menor_cre = matricula, cre
    soma += cre
    cont += 1
    matricula = str(input())
    if matricula != '999':
        cre = float(input())
print(pior)
print(f'{soma / cont:.2f}')