'''
try: 

except tipo_de_exceção

else: < opcional >

finally: < opcional >

'''

# Exemplo (Sem tratamento de erro)

num = int(input('Número: '))
print(f'Você digitou o número {num}')

# Exemplo (Sem tratamento de erro) 2

teste = 1

while teste !=0:

    try:
        num = int(input('Número: '))
        print(f'Você digitou o número {num}')
    except ValueError:
        print('Entrada inválida! Por favor, digite um número')
    
    teste = int(input('Deseja continuar? 1 - Continuar, 0 - Sair'))