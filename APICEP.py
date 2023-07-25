'''
Via CEP
https://viacep.com.br/

'''

# Consulta de Informações de um CEP
import requests


cep = "94500200"

link = f"https://viacep.com.br/ws/{cep}/json/"

requisicao = requests.get(link)

dic_requisicao = requisicao.json()

uf = dic_requisicao['uf']
cidade = dic_requisicao['localidade']
bairro = dic_requisicao['bairro']

print(f'{bairro}, {cidade}, {uf}')


# Busca de CEP a partir de um endereço


