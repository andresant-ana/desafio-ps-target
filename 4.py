faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = 0.0

for estado in faturamento:
    faturamento_total += faturamento[estado]

for estado in faturamento:
    percentual = (faturamento[estado] / faturamento_total) * 100
    print(f"Percentual de representação de {estado}: {percentual:.2f}%")