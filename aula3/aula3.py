# x = int(input("qual valor de x: "))
# y = int(input("qual valor de y: "))

# if x > y :
#     print("x maior que y")
# else:
#     print("y maior que x")


x = int(input("qual valor de x: "))
y = int(input("qual valor de y: "))

z = divmod(x,y)

if z[1] == 0:
    print("par em divmod")
else:
    print("impar em divmod")
print (f'{z[0]}   {z[1]}')

if x % y == 0:
    print("par em check %")
elif x % y == 1: 
    print("impar em check %")
