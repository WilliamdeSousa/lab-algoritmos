idade = int(input())
if idade < 5:
    print('Idade invalida.')
elif idade < 8:
    print('Infantil A')
elif idade < 11:
    print('Infantil B')
elif idade < 14:
    print('Juvenil A')
elif idade < 18:
    print('Juvenil B')
elif idade < 41:
    print('Adulto')
else:
    print('Master')
