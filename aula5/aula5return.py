s1 = input('escreva uma palavra: ')
minInput = int(input('qual valor min: '))
maxInput = int(input('qual valor max: '))
def checkStr(minV, maxV ,paravra = ""):
    try:
        return len(paravra) >= minV and len(paravra) <= maxV
    except Exception as e:
        print(e)


print (checkStr(minInput, maxInput, s1))