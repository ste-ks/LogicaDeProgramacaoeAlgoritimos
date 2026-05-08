# x = int(0)
# while x  <= 5:
#     print(x)
#     x += 1

# for x in range(1, 6):
#     print(x)




# x = int(input("digite a quantidade de iterações: "))
# y = int(input("comecar a contagem a partir de "))
# i = int(y)
# while i < x:
#     print((i) if (i%2)== 0 else '')
#     i += 1

# # for i in range(y, x):
# #     print((i) if (i%2)== 0 else '')



# y = float(0)
# i = int(1)
# while i <= 5:
#     x = float(input("qual a nota: "))
#     y = float(x + y)
#     print((f' media de {y/5:.2f}') if (i == 5) else (f'nota {y}'))
#     i += 1

# for i in range(1,6):
#     x = float(input("qual a nota: "))
#     y += x
#     print((f'a media foi {y/5:.2f}') if i == 5 else (f'a nota foi {y}'))



# --------------------------------------------------------------------------------------------------


# x = 1
# while (x % 2) != 0 or (x <= 0):
#     x = int(input("digite um valor par: "))
#     if (x <= 0):
#         print('nao pode ser menor igual a zero')
#     elif (x % 2) != 0:
#         print('nao pode ser impar')
x = 1
# while True:
#     x = int(input("digite um valor par: "))
#     if (x <= 0):
#         print('nao pode ser menor igual a zero')
#     elif (x % 2) != 0:
#         print('nao pode ser impar')
#     elif (x % 2) == 0:
#         break


# s1 = ''
# while True:
#     s1 = input('digite qualquer texto \n caso queira encerrar digite "sair" ')
#     sv = s1.lower()
#     if sv == 'sair':
#         break
#     else:
#         continue
#     print('nao pode ser impresso')


# nome = ''
# valor = 0
# while True:
#     nome = input('qual o nome: ')
#     if nome:
#         valor = int(input('qual valor: '))
#         if valor:
#             break
#         else:
#             continue
#     else:
#         continue

# --------------------------------------------------------------------------------------------------


# for i in range (1,6,10):
#     print(f'{i}')

# frase = "Lógica de Programação e Algoritmos"
# for i in range(0, len(frase), 1):
#      print(frase[i], end='1 1')
'''em print colocando o parametro end='' remove-se a quebra de linha inserindo todos print na mesma linha no terminal '''

# for i in frase:
#     print(i, end='')

# soma = 0
# quantidade = 0
# for i in range (1,101,1):
#     if (i % 2) == 0:
#         soma += i
#         quantidade += 1
# print(f' a media é {soma / quantidade}')


# --------------------------------------------------------------------------------------------------
soma = 0
produto = 0
# for i in range(1,11,1):
#     soma += i
#     for i2 in range(1,11,1):
#         #produto = soma * i2
#         print(f'{soma * i2}', end='')
#     print('\n')
# print(soma)

# for i in range(1,11,1):
#     soma += i
#     print('soma ', f'{soma}')
#     print('i ', f'{i}')
#     for i2 in range(1,11,1):
#         #produto = soma * i2
#         # print(f'{i * i2}', end=' ')
#         print(f'{i} X {i2} = {i * i2}')
#     print('\n')
# print(soma)



# def div2 (num, den):
#         res = num / den
#         print(res)
#         return ''

# print(div2(3, 10))


def parangaricu():
      palavra1 = 'parangaricu'
      tirimirruaro(palavra1)

def tirimirruaro(palavra):
      palavra2 = palavra + 'tirimirruaro'
      print(palavra2)

parangaricu()
print(tirimirruaro('dsa    '))