espaco = str(input()) == 'A'
porta_malas = str(input()) == 'G'

req_opcionais = 0
if float(input()) < 100000:
    req_opcionais += 1
if float(input()) >= 1.5:
    req_opcionais += 1
if str(input()) == 'A':
    req_opcionais += 1

if espaco and porta_malas:
    if req_opcionais == 0:
        print('Recomendo pensar melhor...')
    elif req_opcionais == 1:
        print('Pode ser uma opção.')
    elif req_opcionais == 2:
        print('Boa compra.')
    elif req_opcionais == 3:
        print('Pode comprar!')
else:
    print('Não compre!')