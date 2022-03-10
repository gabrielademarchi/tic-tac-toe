
running = True

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def print_board():
    for posicao in board:
        print(posicao)


def ask_for_linha():
    while True:
        try:
            nova_linha = int(input('Qual linha? selecione 1, 2, 3: '))
            if (nova_linha <= 0 or nova_linha > 3):
                print('Escolha entre 1, 2 ou 3')
                continue
        except ValueError:
            print('Tente de novo')
            continue
        else:
            return nova_linha


def ask_for_coluna():
    while True:
        try:
            nova_coluna = int(input('Qual coluna? selecione 1, 2, 3: '))
            if (nova_coluna <= 0 or nova_coluna > 3):
                print('Escolha entre 1, 2 ou 3')
                continue
        except ValueError:
            print('Tente de novo')
            continue
        else:
            return nova_coluna


def score():
    for posicao in range(3):
        if ((board[posicao][0] == board[posicao][1] == board[posicao][2] != ' ') or
                (board[0][posicao] == board[1][posicao] == board[2][posicao] != ' ') or
                (board[0][0] == board[1][1] == board[2][2] != ' ') or
                (board[0][2] == board[1][1] == board[2][0] != ' ')):
            return True


# GAME LOOP
while running:
    print_board()
    i = 0
    while i < 9:
        linha = ask_for_linha()
        coluna = ask_for_coluna()

        if board[linha-1][coluna-1] != ' ':
            print('essa posição já foi ocupada, escolha outra')
            i -= 1
        else:
            if (i % 2) == 0:
                marcador = 'X'
            else:
                marcador = 'O'

            board[linha-1][coluna-1] = marcador
            print_board()
            score()
            if score():
                print(f'fim de jogo, o jogador {marcador} ganhou')
                break
        i += 1

    #print('fim de jogo, deu empate')
    running = False
