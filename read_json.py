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
auth[0]['notificacao']
auth[0]['medicamentos']
auth[0]['reacoes']
auth[0]['doencasConcomitantes']
