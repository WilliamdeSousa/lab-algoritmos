tipo = str(input())
valor = float(input())
if tipo != 'PP' and tipo != 'PPF' and tipo != 'PPJ':
    print('Despesa inválida.')
else:
    if tipo != 'PP':
        rubrica = str(input())
        if tipo == 'PPF':
            if rubrica != 'SERV':
                print('Pessoa física não pode fornecer materiais para o serviço público.')
            elif valor > 8000:
                print('Excesso de pagamento para pessoa física.')
            else:
                print('Pagamento liberado.')
        else:
            if rubrica == 'CAP' and valor > 5000000:
                print('O valor para pagamento da rubrica de capital não pode exceder R$ 5M.')
            elif rubrica == 'CUST' and valor > 2000000:
                print('O valor para pagamento da rubrica de custeio não pode exceder R$ 2M.')
            elif rubrica == 'SERV' and valor > 500000:
                print('O valor para pagamento da rubrica de serviços não pode exceder R$ 500K.')
            else:
                print('Pagamento liberado.')
    else:
        if valor > 4000:
            print('Excesso de pagamento para pessoal.')
        else:
            print('Pagamento liberado.')
