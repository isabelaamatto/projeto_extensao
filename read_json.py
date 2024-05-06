import json

# Ler arquivo
with open('amostraNotificacoesRecebidas.json') as f:
    auth = json.load(f)

# exibir conteudo do arquvo
auth

# tamanho do arquivo
len(auth)

# O arquivo foi lido como lista de dicionarios
# mostrar chave to primeiro item
auth[0].keys()

# exibir os valores para cada chave
auth[1]['notificacao']
auth[1]['medicamentos']
auth[1]['reacoes']
auth[1]['doencasConcomitantes']

