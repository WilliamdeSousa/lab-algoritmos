preco = float(input())
print(f'''A vista com desconto de 10%: {preco * 0.9:.2f}
Valor da parcela em 3x sem juros: {preco / 3:.2f}
Comissao do vendedor a vista: {preco * 0.9 * 0.05:.2f}
Comissao do vendedor a prazo: {preco * 0.05:.2f}''')