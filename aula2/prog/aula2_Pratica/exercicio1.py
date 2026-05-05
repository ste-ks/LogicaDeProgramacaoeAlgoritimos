valor_Produto = float(input('qual valor do produto: '))
valor_Desconto = float(input('qual valor do desconto: '))
print(f'valor com desconto é {valor_Produto - (valor_Produto * valor_Desconto / 100.0)}, o desconto é de {valor_Desconto}% e você economiza {(valor_Produto * valor_Desconto / 100.0)} do original de {valor_Produto}')