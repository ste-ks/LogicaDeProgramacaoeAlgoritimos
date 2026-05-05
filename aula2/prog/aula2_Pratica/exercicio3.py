s1 = input("Digite seu texto: ")
iSizeS1 = len(s1)
s2 = s1[:(int(iSizeS1 /2))]
iSizeS2 = len(s2)
print(f'tamanho da string escrita é {iSizeS1} o corte até a metade é {s2} e os 2 ultimos caracteres do corte é {s2[(iSizeS2 - 2):]}')