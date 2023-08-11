velocidade_max = float(input())
velocidade = float(input())
if velocidade <= velocidade_max:
    multa = 0
    pontos = 0
elif velocidade <= round(velocidade_max * 1.2, 2):
    multa = 85.13
    pontos = 4
elif velocidade <= velocidade_max * 1.5:
    multa = 127.69
    pontos = 5
else: 
    multa = 574.62
    pontos = 7
print(f'{multa:.2f}\n{pontos}')
