
try:
    arquivo = open('meu_arquivo.txt', 'r')
    conteudo = arquivo.read()

    print('Arquivo lido com sucesso')
except FileNotFoundError:
    print('Erro: Arquivo não encontrado.')

else:
    print('Nenhum erro ocorreu')

finally:
    arquivo.close()
    print('Arquivo fechado')