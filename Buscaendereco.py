'''
Via CEP
https://viacep.com.br/

'''



# Busca de CEP a partir de um endereço
import requests


uf = 'RS'
cidade = 'Viamão'
endereco = "Rua Alcebíades Azeredo dos Santos"

link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'

requisicao = requests.get(link)
print(requisicao)

dic_requisicao = requisicao.json()
print(dic_requisicao)