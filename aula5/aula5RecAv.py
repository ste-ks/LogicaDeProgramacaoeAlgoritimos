# i = 0
# while True:
#     try:
#         nome = input('Por favor digite o seu nome: ')
#         ind = int(input('Digite um indice do seu nome digitado: ') )
#         print(nome[ind])
#         break
#     except ValueError:
#         print('Oops! Nome invalido. Tente novamente ... ')
#     except IndexError:
#         print('Oops! indice invalido. Tente novamente ... ')
#     finally: #Sempre executa, independente de haver ou nao uma execao
#         print(f'Tentativa {i}')
#         i += 1

# res = lambda x: x*x
# print(res(int(input('digite um valor para elevar ao quadrado: '))))

# res = lambda x,y: x * y
# print(res(int(input('digite o primeiro valor da mul: ')), int(input('digite o segundo valor da mul: ')) ))

res = lambda x,y: (x+5)*y
print(res(int(input('digite o primeiro valor: ')), int(input('digite o segundo: ')) ))