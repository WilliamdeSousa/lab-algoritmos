maior = num = int(input())
while num != 0:
    if num > maior:
        maior = num
    num = int(input())
print(maior)