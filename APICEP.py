'''
Via CEP
https://viacep.com.br/

'''

# Consulta de Informações de um CEP
import requests

# tratamento de string
cep = input(str('Digite o CEP:(Deve conter apenas números) '))
cep = cep.replace('-', '').replace('.', '').replace(' ', '')

if len(cep) == 8:
    link = f"https://viacep.com.br/ws/{cep}/json/"

    requisicao = requests.get(link)

    dic_requisicao = requisicao.json()

    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']

    print(f'{bairro}, {cidade}, {uf}')
    
else:
    print('CEP inválido. Revise o CEP.')


# Busca de CEP a partir de um endereço


