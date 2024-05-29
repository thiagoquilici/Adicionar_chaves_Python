# dicionario
pessoa = {
    'Nome': 'Alex Machado',
    'Idade': 39,
    'Profissão': 'Programador'

}

nova_chave = input('Digite o nome do campo: ')
novo_valor = input('Informe o valor do novo campo: ')
pessoa[nova_chave] = novo_valor

# exibe os dados
for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')