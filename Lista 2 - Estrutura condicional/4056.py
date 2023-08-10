colesterol = float(input())
estado = 'ALTO' if colesterol > 170 else 'LIMITROFE' if colesterol >= 150 else 'DESEJAVEL'
print(f'Colesterol total {colesterol:.1f} mg/dl ({estado})')