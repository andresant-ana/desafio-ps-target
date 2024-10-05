# 1

indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma += k

print(soma)

#===============================================================================

# 2

def is_fibonacci(num):
    a = 0
    b = 1

    while a < num:
        prox_valor = a
        a = b
        b = prox_valor + b

    if a == num:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."
    
numero = int(input("Informe um número: "))
print(is_fibonacci(numero))

#===============================================================================

# 3

import json

def carregar_dados_arquivo(arquivo):
    with open(arquivo, 'r') as f:
        dados = json.load(f)
    return dados

def calcular_faturamento(dados):
    faturamentos = []
    
    for dia in dados:
        if dia['valor'] > 0:
            faturamentos.append(dia['valor'])
    
    if not faturamentos:
        return 0, 0, 0
    
    menor_faturamento = faturamentos[0]
    maior_faturamento = faturamentos[0]
    
    soma_faturamentos = 0
    cont_faturamentos = 0
    
    for f in faturamentos:
        if f < menor_faturamento:
            menor_faturamento = f
        
        if f > maior_faturamento:
            maior_faturamento = f
            
        soma_faturamentos += f
        cont_faturamentos += 1
    
    media_mensal = soma_faturamentos / cont_faturamentos if cont_faturamentos > 0 else 0
    
    dias_acima_media = 0
    for f in faturamentos:
        if f > media_mensal:
            dias_acima_media += 1
    
    return menor_faturamento, maior_faturamento, dias_acima_media

def exibir_resultados(menor_faturamento, maior_faturamento, dias_acima_media):
    print(f"Menor valor de faturamento ocorrido: R${menor_faturamento:.2f}")
    print(f"Maior valor de faturamento ocorrido: R${maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

arquivo_json = '[AQUI VAI O CAMINHO DO ARQUIVO JSON]' # Não inseri o caminho do arquivo para não expor informações sensíveis

dados_faturamento = carregar_dados_arquivo(arquivo_json)

menor_faturamento, maior_faturamento, dias_acima_media = calcular_faturamento(dados_faturamento)

exibir_resultados(menor_faturamento, maior_faturamento, dias_acima_media)

#===============================================================================

# 4

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

#===============================================================================

# 5

string_original = "Olá, mundo!"

string_invertida = ""

for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]

print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")
