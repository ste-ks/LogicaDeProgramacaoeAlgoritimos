kmDrived = float(input("qual a km percorrida: "))
rentDays = int(input("quantos dias de aluguel: "))
'''
60 reais dia
0.15 / km
'''
totalAmount = (kmDrived * 0.15)+(rentDays * 60)
print(f'a kilometragem foi de {kmDrived}km, diaria total de {rentDays}')
print(f'valor de dirarias de {rentDays * 60}R$ e valor total por quilometragem de {kmDrived * 0.15} R$ totalizando {totalAmount}')