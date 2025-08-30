try:
    lista = [1,2,3]

    for n in lista:
        print(f'Elemento:{n}')

    num = int(input('Número: '))
    lista.append(num)

    print(lista[4])
except ValueError:
    print('Erro: Valor inválido inserido, apenas números são aceitos')
except IndexError:
    print('Erro: Índice fora da lista')
except ZeroDivisionError:
    print('Erro: Divisão por ZERO')
except Exception as e:
    print(f'Erro genérico: {e}')

else:
    print('Deu tudo certo!') # Opcional
finally: 
    print('Encerrando o programa. Adeus :(')
    # Opcional: Independente se deu certo ou não, ele executa.