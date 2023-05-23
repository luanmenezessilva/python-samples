import requests
import json
from datetime import datetime


# Busca data e formata em dd-mm-aaaa
hoje = datetime.now().date()
data_atual = hoje.strftime('%m-%d-%Y')

# Faz a requisição na API do Banco Central
url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_atual}'"
response = requests.get(url)
response = json.loads(response.text)

# Pega a cotação de compra e de venda do dia atual
cotacao_compra = response['value'][0]['cotacaoCompra']
cotacao_venda = response['value'][0]['cotacaoVenda']

# Mostra as cotações
print(cotacao_compra)
print(cotacao_venda)