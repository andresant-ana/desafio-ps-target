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