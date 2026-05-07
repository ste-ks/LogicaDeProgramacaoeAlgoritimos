# print((2+2)<4)
# print((7//3)==(1+1))
# print(((3**2)+(4**2))==(25))
# print((2+4+6)>12)
# print("divisivel" if ((1387 % 19) == 0) else (1387 % 19))
# print("par" if (31 % 2)==2 else "impar")

# x = [34,29,31]
# print("menor que 30" if (min(x) < 30) else "maior que 30" )




# idade = int(input("qual idade"))
# print("direto ao beneficio" if (idade > 60) else "sem beneficio")

# dano = float(input("qual o dano: "))
# escudo = float(input("qual defesa: "))
# print("esta morto" if ((dano >10) and (escudo == 0)) else "em batalha")

# norte = bool(int(input("norte: ")))
# sul = bool(int(input("sul: ")))
# leste = bool(int(input("leste: ")))
# oeste = bool(int(input("oeste: ")))

# print("escapou" if (norte or sul or leste or oeste) else "preso")




# ano = int(input("qual o ano: "))
# print("pode ser bissesto" if ((ano % 4) ==0) else 'não é bissesto')

# cima = bool(int(input("posicao cima: ")))
# baixo = bool(int(input("posicao baixo: ")))
# print("indeciso" if (cima and baixo) else "decidido")

# lado1 = float(input("valor do lado 1: "))
# lado2 = float(input("valor do lado 2: "))
# lado3 = float(input("valor do lado 3: "))

# if lado1 == 0.0 or lado2 == 0.0 or lado3 == 0.0:
#     print("não é triangulo")
# elif (lado1 == lado2 == lado3):
#     print("equilátero")
# elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
#     print("isóceles")
# else:
#     print("escaleno")




# var1 = float(input("valor 1: "))
# var2 = float(input("valor 2: "))

# print("qual operacao desejada : \n + \n - \n * \n /")
# operacao = input()

# if operacao == "+":
#     print(var1 + var2)
# elif operacao == "-":
#     print(var1 - var2)
# elif operacao == "*":
#     print(var1 * var2)
# elif operacao == "/":
#     print(var1 / var2)
# else:
#     print("operacao indevida")

# try:
#     expressao = f'{var1} {operacao} {var2}'
#     resutado = eval(expressao)
#     print(f'resutado do calculo foi {resutado}')
# except Exception as e:
# 	print(f'o erro a seguir \n {e}')

# import operator
# # Mapeamos o símbolo para a função real do Python
# operacoes = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv
# }
# var1 = float(input("valor 1: "))
# var2 = float(input("valor 2: "))
# operacao = input("operação (+, -, *, /): ")
# if operacao in operacoes:
#     # Busca a função no dicionário e a executa passando os dois valores
#     resultado = operacoes[operacao](var1, var2)
#     print(f"Resultado: {resultado}")
# else:
#     print("Operação indevida")





consumo = float(input("consumo em kWh: "))
print("r residencial \n i industrial \n c comercio \n")
instal = input()

if instal == "r":
    print( (f'R${consumo * 0.4:.3f}') if (consumo <= 500.0) else (f'R${consumo * 0.65:.3f}'))
elif instal == "i":
    print( (f'R${consumo * 0.55:.3f}') if (consumo <= 5000.0) else (f'R${consumo * 0.6:.3f}'))
elif instal == "c":
    print( (f'R${consumo * 0.55:3f}') if (consumo <= 1000.0) else (f'R${consumo * 0.6:.3f}'))
else:
    print('erro de declaracao')