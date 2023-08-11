# Último lápis
# Importa a função choice do módulo random
from random import choice
from time import sleep

# Imprime a mensagem de início do jogo
print("Jogo do Ultimo Lápis")

# Loop principal do jogo
while True:
    # Solicita ao jogador o número de lápis a serem usados
    lapis = input("Quantos lápis serão usados?\n")

    # Verifica se o valor inserido é numérico
    if not lapis.isnumeric():
        print('O número de lápis deve ser numérico!')
    # Verifica se o número é zero
    elif int(lapis) == 0:
        print('O número de lápis deve ser positivo')
    # Verifica se o número é negativo
    elif int(lapis) < 0:
        print('O número de lápis deve ser positivo')
    else:
        # Converte o valor inserido para um número inteiro e quebra o loop
        lapis = int(lapis)
        break

# Loop para a escolha do modo de jogo
while True:
    try:
        # Solicita ao jogador que escolha um modo de jogo
        opcao = int(input("""Escolha um modo de jogo:
        [1] - Jogador vs Jogador
        [2] - Jogador vs CPU
        Digite: """))

        # Verifica se a opção inserida está dentro das opções válidas
        if opcao not in [1, 2]:
            raise ValueError('Opção inválida')
    except ValueError as erro:
        print(f"Erro: {erro}")
    else:
        # Modo de jogo contra a CPU
        if opcao == 2:
            jogadores = []
            nome1 = input("Nome do primeiro jogador: ").title()
            nome2 = input("Nome da CPU: ").title()
            jogadores.append(nome2)
            jogadores.append(nome1)

            # Loop para determinar quem começa o jogo
            while True:
                print(f"Quem irá começar a jogar {nome1}, {nome2}")
                primeiro = input()
                if primeiro != nome1 and primeiro != nome2:
                    print(f'Escolha entre {jogadores}!')
                else:
                    break

            # Lista de possibilidades de lápis que podem ser pegos
            possibilidades = [list(range(4, lapis + 1, 4)), list(range(3, lapis + 1, 4)),
                              list(range(2, lapis + 1, 4)), list(range(5, lapis + 1, 4))]

            # Imprime os lápis iniciais
            print("|" * lapis)
            contador = 0

            # Início do jogo
            if primeiro == f'{nome1}':
                while lapis > 0:
                    if contador % 2 == 0:
                        print(f"Vez do(a) {nome1}!")
                        sleep(0.5
                              )

                        # Loop para a escolha da quantidade de lápis a serem pegos pelo jogador
                        while True:
                            qauntidade = input()
                            if not qauntidade.isnumeric():
                                print("Valores possíveis (1 2 3), tente novamente!")
                            elif int(qauntidade) > 3 or int(qauntidade) < 1:
                                print("Valores possíveis (1 2 3), tente novamente!")
                            elif int(qauntidade) > lapis:
                                print('Quantidade pegada de lápis excede o montante na mesa!!!')
                            else:
                                break

                        # Atualiza a quantidade de lápis na mesa e imprime a nova configuração
                        lapis -= int(qauntidade)
                        print("|" * lapis)
                        contador += 1

                    # Verifica se o jogador atual ganhou
                    if lapis <= 0:
                        print(f'{nome2} ganhou!')
                        break
                    else:
                        print(f"Vez do(a) {nome2}!")
                        sleep(0.5
                              )
                        # Loop para a escolha da quantidade de lápis a serem pegos pela CPU
                        while True:
                            soma = 0
                            for lista in possibilidades:
                                if lapis in lista:
                                    if soma == 0:
                                        qauntidade = 3
                                        print(qauntidade)
                                        lapis -= qauntidade
                                        print("|" * lapis)
                                        break
                                    elif soma == 1:
                                        qauntidade = 2
                                        print(qauntidade)
                                        lapis -= qauntidade
                                        print("|" * lapis)
                                        break
                                    elif soma == 2:
                                        qauntidade = 1
                                        print(qauntidade)
                                        lapis -= qauntidade
                                        print("|" * lapis)
                                        break
                                    elif soma == 3:
                                        qauntidade = choice(range(1, 3))
                                        print(qauntidade)
                                        lapis -= qauntidade
                                        print("|" * lapis)
                                        break
                                soma += 1
                                if lapis == 1:
                                    print(lapis)
                                    lapis -= 1
                            contador += 1

                            # Verifica se a CPU ganhou
                            if lapis <= 0:
                                print(f'{nome1} ganhou!')
                                break


            # Continuação do código a partir do else no início do jogo
            else:
                while lapis > 0:
                    if contador % 2 == 0:
                        print(f"Vez do(a) {nome2}!")
                        sleep(0.5
                              )
                        # Loop para a escolha da quantidade de lápis a serem pegos pela CPU
                        while True:
                            soma = 0
                            for lista in possibilidades:
                                if lapis in lista:
                                    if soma == 0:
                                        qauntidade = 3
                                        print(qauntidade)
                                        lapis -= qauntidade
                                        print("|" * lapis)
                                        break
                                    elif soma == 1:
                                        qauntidade = 2
                                        print(qauntidade)
                                        lapis -= qauntidade
                                        print("|" * lapis)
                                        break
                                    elif soma == 2:
                                        qauntidade = 1
                                        print(qauntidade)
                                        lapis -= qauntidade
                                        print("|" * lapis)
                                        break
                                    elif soma == 3:
                                        qauntidade = choice(range(1, 3))
                                        print(qauntidade)
                                        lapis -= qauntidade
                                        print("|" * lapis)
                                        break
                                soma += 1
                                if lapis == 1:
                                    print(lapis)
                                    lapis -= 1
                            break
                        contador += 1
                        if lapis <= 0:
                            print(f'{nome1} ganhou!')
                            break
                    else:
                        print(f"Vez do(a) {nome1}!")
                        sleep(0.5
                              )
                        # Loop para a escolha da quantidade de lápis a serem pegos pelo jogador
                        while True:
                            qauntidade = input()
                            if not qauntidade.isnumeric():
                                print("Valores possíveis (1 2 3), tente novamente!")

                            elif int(qauntidade) > 3 or int(qauntidade) < 1:
                                print("Valores possíveis (1 2 3), tente novamente!")
                            elif int(qauntidade) > lapis:
                                print('Quantidade pegada de lápis excede o montante na mesa!!!')
                            else:
                                break
                        lapis -= int(qauntidade)
                        print("|" * lapis)
                        contador += 1
                    if lapis <= 0:
                        print(f'{nome2} ganhou!')
                        break


        # Continuação do código a partir do ponto em que o valor do 'primeiro' é diferente de 'nome1'

        else:
            jogadores = []
            nome1 = input("Nome do primeiro jogador: ").title()

            nome2 = input("Nome do segundo jogador: ").title()
            jogadores.append(nome2)
            jogadores.append(nome1)
            # Loop para determinar quem começa o jogo
            while True:
                print(f"Quem irá começar a jogar {nome1}, {nome2} ")
                primeiro = input()
                if primeiro != nome1 and primeiro != nome2:
                    print(f'Escolha entre {jogadores}!')
                else:
                    break

            # Lista de possibilidades de lápis que podem ser pegos
            possibilidades = [list(range(4, lapis + 1, 4)), list(range(3, lapis + 1, 4)),
                              list(range(2, lapis + 1, 4)), list(range(5, lapis + 1, 4))]
            # Imprime os lápis iniciais
            print("|" * lapis)
            contador = 0
            while lapis > 0:
                if contador % 2 == 0:
                    print(f"Vez do(a) {nome2}!")
                    sleep(0.5
                          )
                    while True:
                        qauntidade = input()
                        if not qauntidade.isnumeric():
                            print("Valores possíveis (1 2 3), tente novamente!")
                        elif int(qauntidade) > 3 or int(qauntidade) < 1:
                            print("Valores possíveis (1 2 3), tente novamente!")
                        elif int(qauntidade) > lapis:
                            print('Quantidade pegada de lápis excede o montante na mesa!!!')
                        else:
                            break
                    lapis -= int(qauntidade)
                    print("|" * lapis)
                    contador += 1
                if lapis <= 0:
                    print(f'{nome1} ganhou!')
                    break
                else:
                    print(f"Vez do(a) {nome1}!")
                    sleep(0.5
                          )
                    while True:
                        qauntidade = input()
                        if not qauntidade.isnumeric():
                            print("Valores possíveis (1 2 3), tente novamente!")
                        elif int(qauntidade) > 3 or int(qauntidade) < 1:
                            print("Valores possíveis (1 2 3), tente novamente!")
                        elif int(qauntidade) > lapis:
                            print('Quantidade pegada de lápis excede o montante na mesa!!!')
                        else:
                            break
                    lapis -= int(qauntidade)
                    print("|" * lapis)
                    contador += 1
                if lapis <= 0:
                    print(f'{nome2} ganhou!')
                    break
    break
