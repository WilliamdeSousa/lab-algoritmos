ph = float(input('Digite o pH da solucao:\n'))
if ph < 0 or ph > 14:
    print('Valor deve estar entre 0 e 14.')
elif ph < 7:
    print('Essa solucao e acida.')
elif ph > 7:
    print('Essa solucao e basica.')
else:
    print('Essa solucao e neutra.')