num = int(input())
cont = soma = 0
while num != 0:
    cont += 1
    soma += num
    num = int(input())
media = soma // cont
print(media)