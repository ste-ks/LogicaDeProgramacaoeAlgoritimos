# mochila = ('item1','item2','item3','item4')
# print (f'{mochila[0]}')
# print (f'{mochila[1]}')
# print (f'{mochila[2]}')
# print (f'{mochila[3]}')
# print (f'{mochila[:2]}')
# print (f'{mochila[2:]}')
# print (f'{mochila[-1]}')

# for i in mochila:
#     print(f'{i}')

# for i in range (len(mochila)):
#     print(f'{mochila[i]}')

# addMochila = ('item5','item6','item7')
# total = mochila + addMochila
# print (total)

# -------------------------------------------

# def soma(*numTupla):
#     total = 0
#     for i in numTupla:
#         total += i
#     return total
# tuplaNum = (1,1,1,1,1,1,1,1,1,10)
# print (f'{soma(*tuplaNum)}')
# print (f'{soma(1,1,1,1,1,1,1,1,1,10)}')


# --------------------------------------------------------------------------------------------------------------------
# mochila = ['item1','item2','item3','item4']
# print (f'{mochila}')
# mochila[1] = 'novo item'
# print (f'{mochila}')
# mochila.append('item5')
# print (f'{mochila}')
# mochila.insert(1, 'item2')
# print (f'{mochila}')
# # del mochila[2]
# mochila.pop(2)
# # mochila.remove('novo item')
# print (f'{mochila}')
# mochila.clear()
# print (f'{mochila}')
# -------------------------------------------
#mesma referência
# lista_original = [5,7,9,11]
# lista_referenciada = lista_original #e enviado o endereco da memoria, nao cria uma nova memoria
# lista_referenciada = lista_original[:] # o elemento [:] referencia que copiou todo conteudo da lista, cria uma nova memoria
# print(lista_original)
# print(lista_referenciada)
# lista_referenciada[0] = 2
# print(lista_original)
# print(lista_referenciada) 
# -------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
# for i in mochila:
#     for i1 in i:
#         print(f'{i1}')



# mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
# for i in range(0,len(mochila),1):
#         for j in range(0,len(mochila[i]),1):
#             print (mochila [i][j], end='')
#             print (mochila [i][j])
#         print()


# item = []
# item = list()
# lista = []
# quantidade = int(input('quantos produtos a serem cadastrados: '))
# for i in range (0, quantidade, 1):
#     item.append(input('nome do item: '))
#     item.append(input('quantidade do item: '))
#     item.append(input('valor do item: '))
#     lista.append(item[:])
#     item.clear()
# print(lista)

# for i in lista:
#     print(i)

# for i in lista:
#     for i2 in i:
#         print (i2)

# -------------------------------------------
# mercado = list()
# quantidade = int(input('quantos produtos a serem cadastrados: '))
# for i in range(0,quantidade,1):
#     nome = input('qual item: ')
#     qtd = int(input('qual quantidade: '))
#     prec = float(input('qual preco: '))
#     mercado.append([nome,qtd,prec])
# print(mercado)


# soma = 0
# print('Lista de compras:')
# print('-' * 20)
# print('item | quantidade | valor unitario | total do item')
# for item in mercado:
#     print('{} | {} | {}| {}'.format(item[0], item[1], item[2], item[1] * item[2]))
#     soma += item[1] * item[2]
# print('-' * 20)
# print(f'Total a ser pago: {soma}')

# --------------------------------------------------------------------------------------------------------------------
# mochila = ('Laptop', 'Smartphone', 'Power Bank', 'Carregadores e Cabos')
# print('Tupla: ', mochila)

# mochila = ['Laptop', 'Smartphone', 'Power Bank', 'Carregadores e Cabos']
# print('Lista: ', mochila)

# mochila = {'Laptop':1, 'Smartphone':2, 'Power Bank':3, 'Carregadores e Cabos':4}
# print('Dicionario: ', mochila)
# -------------------------------------------
# game = {'nome' : 'Super Mario',
# 'desenvolvedora' : 'Nintendo',
# 'ano' : 1990}
# print(game)
# print(game.get('nome'))
# print(game['nome'])
# print(game.get('desenvolvedora'))
# print(game['desenvolvedora'])
# print(game['ano'])
# print(game.get('ano'))

# print(game.values())
# for i in game.values():
#     print(i)
# print(game.keys())
# for i in game.keys():
#     print(i)
# print(game.items())
# for i in game.items():
#     print(i)
# for i in game.items():
#     for j in i:
#         print(j)

# for chave, valor in game.items():
#     print(f'Chave: {chave} -> Valor: {valor}')

# -------------------------------------------

# games = []
# game1 = {
#     'nome': 'Super Mario',
#     'videogame' : 'Super Nintendo',
#     'ano' : 1990
#     }
# game2 = {
#     'nome':'Zelda Ocarina of Time',
#     'videogame': 'Nintendo 64',
#     'ano':1998
#     }
# game3 = {
#     'nome': 'Pokemon Yellow',
#     'videogame' : 'Game Boy',
#     'ano' : 1999
#     }
# games = [game1, game2, game3]
# print(games)
# -------------------------------------------

# Listas com dicionários
#  - Uma lista contendo, em cada índice, um dicionário

# game = {}
# games = []

# for i in range(3):
#     game['nome'] = input('Qual o nome do jogo?')
#     game['videogame'] = input('Para qual video-game ele foi lançado?')
#     game['ano'] = input('Qual o ano de lancamento?')
#     games.append (game.copy())
# print('-' * 20)
# for jogos in games:
#     for chave, valor in jogos.items():
#         print(f'O campo {chave} tem o valor {valor}.')
# -------------------------------------------

# Dicionários com listas
#  - Um dicionário contendo, em cada índice, uma lista

# games = {
#     'nome': ['Super Mario', 'Zelda Ocarina of Time', 'Pokemon Yellow'],
#     'videogame': ['Super Nintendo', 'Nintendo 64', 'Game Boy'],
#     'ano': [1990,19998,1999]
#     }
# print(games)

# games = {'nome' : [], 'videogame' : [], 'ano' : []}
# for i in range(3):
#     nome = input('Qual o nome do jogo?')
#     videogame = input('Para qual video-game ele foi lançado?')
#     ano = input('Qual o ano de lancamento?')
#     games['nome'].append (nome)
#     games['videogame'].append(videogame)
#     games['ano'].append (ano)
# print('-' * 20)
# print(games)
# -------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

# s1 = list('texto')
# print(s1)
# print(''.join(s1))
# s1[0] = 'T'
# print(''.join(s1))
# -------------------------------------------

s1 = 'Logica de Programacao e Algoritmos'
s2 = '123'
# print(s1.startswith('Logica'))
# print(s1.endswith('Algoritmos'))
# print(s1.lower().endswith('algoritmos'))
# print(s1.lower())
# print(s1.upper())
# print(s1.count('a'))
# print(s1.lower().count('a'))
# print(s1.split(' '))
# print(s1.lower().replace('logica', 'teste', count=1))
print(s1.isalnum()) #como possui espaco nao retorna verdadeiro
print(s2.isalnum())
print(s1.isalpha())
print(s2.isalpha())


# -------------------------------------------
# -------------------------------------------