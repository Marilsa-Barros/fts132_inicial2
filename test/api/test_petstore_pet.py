import pytest
import requests

base_url ='https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}

def testar_incluir_pet():
    # Configura
    # Dados de entrada vem do Json
    status_code_esperado = 200
    nome_pet_esperado = 'Mag'
    tag_esperada = 'Vacinado'

    # Executa
    resposta = requests.post(
    url=base_url,
    data=open('C:/Users/Tata/PycharmProjects/fts132_inicial2/test/db/pet1.json', 'rb'),
    headers=headers
    )

    # Formata
    print(resposta)
    print(resposta.status_code)
    corpo_da_resposta = resposta.json()
    print(corpo_da_resposta)

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    #assert corpo_da_resposta['tags.name'] == tag_esperada

def testar_consultar_pet():
    status_code = 200
    id = 1080
    name = 'Mag'

    resposta = requests.get(
        url=f'{base_url}/{name}',
        headers=headers
    )

    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    assert resposta.status_code == status_code
    assert corpo_da_resposta['id'] == id
    assert corpo_da_resposta['name'] == name



