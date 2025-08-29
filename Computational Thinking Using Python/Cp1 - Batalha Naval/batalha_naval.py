cordenadas_navios = []


def montar_tabuleiro():
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]

    # Imprimindo a estutura

    print("   ", end = " ")

    # Imprimindo o cabeçalho do alfabeto
    for i in alfabeto:
        print(f"{i} ", end = " ")

    # Imprimindo a descrição das linhas e o valores respectivo de ambos, linhas e colunas 
    print("")

    for i in numeros:
        
        if i >= 10:
            print(f"{i}  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o")
        else:
            print(f"O{i}  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o")


    # Fazer uma lista imprimir a linha


'''
Batalha Naval - Etapas para a construção lógica

Menus:

//// Menu inicial

    1.Iniciar
    2.Placar
    3.Sair

(Jogador 1) : Insira os navios no tabuleiro

    A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  
O1  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O2  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O3  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O4  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O5  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O6  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O7  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O8  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O9  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
10  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
11  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
12  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
13  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
14  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
15  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o

• Escolha uma letra ( A  B  C  D  E  F  G  H  I  J  K  L  M  N  O):
    
• Escolha um número (O1,O2,O3,O4,O5,O6,O7,O8,O9,1O,11,12,13,14,15):

    
(Jogador 2) : Insira a posição dos navios
• Escolha uma letra ( A  B  C  D  E  F  G  H  I  J  K  L  M  N  O):
    
• Escolha um número (O1,O2,O3,O4,O5,O6,O7,O8,O9,1O,11,12,13,14,15):

//// Partida Iniciada

    A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  
O1  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O2  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O3  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O4  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O5  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O6  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O7  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O8  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
O9  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
10  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
11  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
12  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
13  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
14  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o
15  o  o  o  o  o  o  o  o  o  o  o  o  o  o  o








'''