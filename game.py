from time import sleep


def draw(m):
    for i in m:
        for j in i:
            if j == 0:
                j = " "
            print(f"|{j}", end="")
        print("|")


def game_matrix(c_p, m, p_i, p_j, p_c):
    for i in range(len(m)):
        for j in range(len(m)):
            m[p_i][p_j] = c_p

    if c_p == "X":
        c_p = "O"
        p_c += 1
    elif c_p == "O":
        c_p = "X"
        p_c += 1

    return m, c_p, p_c


def check_player_winner(m):
    if (m[0][0] == "X" and m[0][1] == "X" and m[0][2] == "X") or (
            m[1][0] == "X" and m[1][1] == "X" and m[1][2] == "X") or (
            m[2][0] == "X" and m[2][1] == "X" and m[2][2] == "X") or (
            m[0][0] == "X" and m[1][0] == "X" and m[2][0] == "X") or (
            m[0][1] == "X" and m[1][1] == "X" and m[2][1] == "X") or (
            m[0][2] == "X" and m[1][2] == "X" and m[2][2] == "X") or (
            m[0][0] == "X" and m[1][1] == "X" and m[2][2] == "X") or (
            m[0][2] == "X" and m[1][1] == "X" and m[2][0] == "X"):
        return "X"

    if (m[0][0] == "O" and m[0][1] == "O" and m[0][2] == "O") or (
            m[1][0] == "O" and m[1][1] == "O" and m[1][2] == "O") or (
            m[2][0] == "O" and m[2][1] == "O" and m[2][2] == "O") or (
            m[0][0] == "O" and m[1][0] == "O" and m[2][0] == "O") or (
            m[0][1] == "O" and m[1][1] == "O" and m[2][1] == "O") or (
            m[0][2] == "O" and m[1][2] == "O" and m[2][2] == "O") or (
            m[0][0] == "O" and m[1][1] == "O" and m[2][2] == "O") or (
            m[0][2] == "O" and m[1][1] == "O" and m[2][0] == "O"):
        return "O"


def game_loop():
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    player_start = str(input("Quem começa jogando? (X/O): ")).upper()
    count_plays = 0

    # Game Loop
    while True:
        if player_start == "X" or player_start == "O":
            print("-=" * 45 + "-")
            print(f"Vez do jogador: {player_start}")
            pos_i = int(input("Digite a posição da linha(i): "))
            if pos_i == -1:
                break
            pos_j = int(input("Digite a posição da coluna(j): "))
            if pos_j == -1:
                break

            if pos_i > 2 or pos_i < 0 or pos_j > 2 or pos_j < 0:
                print("-=" * 45 + "-")
                print("Posição inválida")
            else:
                if matrix[pos_i][pos_j] != 0:
                    print("-=" * 45 + "-")
                    print("Essa posição já está preenchida")
                else:
                    matrix, player_start, count_plays = game_matrix(player_start, matrix, pos_i, pos_j, count_plays)
                    player_winner = check_player_winner(matrix)
                    draw(matrix)

                    if player_winner == "X":
                        print("-=" * 45 + "-")
                        print("O jogador X ganhou!")
                        print("-=" * 45 + "-")
                        print("Saindo...")
                        sleep(3)
                        break
                    elif player_winner == "O":
                        print("-=" * 45 + "-")
                        print("O jogador O ganhou!")
                        print("-=" * 45 + "-")
                        print("Saindo...")
                        sleep(3)
                        break
                    elif count_plays == 9:
                        print("-=" * 45 + "-")
                        print("Deu empate!")
                        print("-=" * 45 + "-")
                        print("Saindo...")
                        sleep(3)
                        break
        else:
            print("-=" * 45 + "-")
            print("Jogador não encontrado")
            print("-=" * 45 + "-")
            player_start = str(input("Quem começa jogando? (X/O): ")).upper()
    return


def game_manual():
    while True:
        print("-=" * 45 + "-")
        print("""
                   _____                             .__   
          /     \ _____    ____  __ _______  |  |  
         /  \ /  \\__  \  /    \|  |  \__  \ |  |  
        /    Y    \/ __ \|   |  \  |  // __ \|  |__
        \____|__  (____  /___|  /____/(____  /____/
                \/     \/     \/           \/      
                """)
        print("-=" * 45 + "-")
        print("1° O jogo é composto por dois jogadores X e O")
        print("2° Para sair no meio da partida, basta digitar -1")
        print("3° Podem ser informadas as posições 0, 1, 2 para linhas(i) e para colunas(j)")
        print("-=" * 45 + "-")

        menu_exit = int(input("Deseja sair? Digite -1: "))
        if menu_exit == -1:
            break
        else:
            print("-=" * 45 + "-")
            print("Não foi possível encontrar a opção informada")
    return


# Main Loop
while True:
    print("-=" * 45 + "-")
    print("""
     ____.                           .___         ____   ____     .__  .__            
    |    | ____   ____   ____      __| _/____     \   \ /   /____ |  | |  |__ _____   
    |    |/  _ \ / ___\ /  _ \    / __ |\__  \     \   Y   // __ \|  | |  |  \\__  \  
/\__|    (  <_> ) /_/  >  <_> )  / /_/ | / __ \_    \     /\  ___/|  |_|   Y  \/ __ \_
\________|\____/\___  / \____/   \____ |(____  /     \___/  \___  >____/___|  (____  /
               /_____/                \/     \/                 \/          \/     \/ 
    """)
    print("-=" * 45 + "-")
    print("""
[0] Começar o Jogo
[1] Ler o Manual
[2] Sair do Jogo
    """)
    options = int(input("Digite uma opção: "))

    if options == 0:
        print("-=" * 45 + "-")
        print("Começando o Jogo. Aguarde...")
        print("-=" * 45 + "-")
        sleep(3)
        game_loop()
    elif options == 1:
        game_manual()
    elif options == 2:
        break
    else:
        print("-=" * 45 + "-")
        print("Não foi possível encontrar a opção informada")
