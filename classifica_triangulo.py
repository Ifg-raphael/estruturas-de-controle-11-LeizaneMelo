#Ler as entradas
a, b, c = map(int, input('Digite o valor de A, B e C (separado por espaço): ' ).split())

#Verificar se forma um triânguloc
if a < b + c and b < a + c and c < a + b:
#Verifica qual tipo de triângulo
    if a == b and b == c:
        print('equilátero')
    elif a == b or b == c or a == c:
        print('isósceles')
    else:
        print ('escaleno')
#Se não formar um triângulo, mostrar msg informando
else:
    print('Não forma triângulo')



