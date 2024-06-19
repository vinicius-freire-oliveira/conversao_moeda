# Importando a classe ExtratorURL do arquivo extracao_url.py
from extracao_url import ExtratorURL

# Conversão de dólar para real
VALOR_DOLAR = 5.05  # 1 dólar = 5.05 reais

# URL para a conversão de moedas
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"

# Cria uma instância do objeto ExtratorURL com a URL fornecida
extrator_url = ExtratorURL(url)

# Obtém os valores dos parâmetros 'moedaOrigem', 'moedaDestino' e 'quantidade' usando o objeto extrator_url
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

# Verifica a conversão de moeda e imprime o resultado
if moeda_origem == "real" and moeda_destino == "dolar":
    valor_conversao = int(quantidade) / VALOR_DOLAR
    print("O valor de R$" + quantidade + " reais é igual a $" + str(valor_conversao) + " dólares.")
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_conversao = int(quantidade) * VALOR_DOLAR
    print("O valor de $" + quantidade + " dólares é igual a R$" + str(valor_conversao) + " reais.")
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")
