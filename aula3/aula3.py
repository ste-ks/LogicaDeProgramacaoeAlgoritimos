# x = int(input("qual valor de x: "))
# y = int(input("qual valor de y: "))

# if x > y :
#     print("x maior que y")
# else:
#     print("y maior que x")


# x = int(input("qual valor de x: "))
# y = int(input("qual valor de y: "))

# z = divmod(x,y)

# if z[1] == 0:
#     print("par em divmod")
# else:
#     print("impar em divmod")
# print (f'{z[0]}   {z[1]}')

# if x % y == 0:
#     print("par em check %")
# elif x % y == 1: 
#     print("impar em check %")


# n1 = float(input("qual a media da materia1 :"))
# n2 = float(input("qual a media da materia2 :"))
# n3 = float(input("qual a media da materia3 :"))
# mf = (n1+n2+n3)/3
# # if mf >= 7.0:
# #     res = "aprovado"
# # else:
# #     res = "reprovado"
#
# print(f'{n1} {n2} {n3} {mf}')
# print ("aprovado" if mf >= 7.0 else "reprovado")


# print("1 = maça \n 2 = laranja \n 3 = banana")
# fruta = int(input("qual fruta: "))# 1 maca, 2 laranja, 3 banana
# quant = int(input("quantidade: "))
# preco = (quant * 2.3) if (fruta == 1) else (quant * 3.6) if (fruta == 2) else (quant * 1.85) if (fruta == 3) else  'escolha de fruta não cadastrada'
# #
# # print(f'R${preco:.2f}')
# print(f'{preco}')


nome = input("qual seu nome: ")
idade = int(input("qual sua idade: "))
print ( ("Vinicios") if (nome == "Vinicios") else ("novinho") if (idade < 18) else ("morto") if (idade > 100) else ("adulto"))