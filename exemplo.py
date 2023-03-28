numero1= float(input('Primeiro Numero:'))
numero2= float(input('segundo numero:') )

print('1 -soma')
print('2 -subtração')
print('3 -multiplicação')
print('4 -divisão')


opcao = int(input('escolha uma opcao:'))

if opcao == 1:
    resultado = numero1 + numero2
    print(f'a soma de {numero1} e {numero2} é {resultado}')
elif opcao == 2:
    resultado = numero1 - numero1
    print(f'a subtracao de {numero1} e {numero2} é {resultado}')
elif opcao == 3:
    resultado = numero1 * numero2
    print(f'a multiplicação de {numero1} e {numero2} é {resultado}')
elif opcao == 4:
    if numero2 != 0:
        resultado = numero1 / numero2 
        print(f'a divisao de {numero1} e {numero2} é {resultado}')
    else:
        print('ERRO: não é possivel fazer uma divisao por zero')
else:
    print('opcao invalida')

