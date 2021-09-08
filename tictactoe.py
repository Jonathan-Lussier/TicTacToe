# jonathan Lussier 2021
import numpy as np

def main():

    print("running\n")

    def check_for_gameover(bdinput):
        winner = 0
        for i in range(3):
            if np.all(bdinput[:, i] == bdinput[1, i]) and bdinput[1, i]:
                if bdinput[1, i] == 1:
                    print("winner is player 1")
                elif bdinput[1, i] == 2:
                    print("winner is player 2")
                else:
                    print("unexpected output!")
                winner = 1
                return winner

            if np.all(bdinput[i, :] == bdinput[i, 1]) and bdinput[i, 1]:
                if bdinput[i, 1] == 1:
                    print("winner is player 1")
                elif bdinput[i, 1] == 2:
                    print("winner is player 2")
                else:
                    print("unexpected output!")
                winner = 1
                return winner

            if np.all(bdinput.diagonal() == bdinput[1, 1]) and bdinput[1, 1]:
                if bdinput[1, 1] == 1:
                    print("winner is player 1")
                elif bdinput[1, 1] == 2:
                    print("winner is player 2")
                else:
                    print("unexpected output!")
                winner = 1
                return winner

        if np.all(bdinput):
            print("cat got it")
            winner = 1
            return winner

        return winner


    def print_board(bdinput):
        # printing the board for the player
        A = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        for i in range(3):
            for j in range(3):
                if bdinput[i, j] == 1:
                    A[i][j] = "X"
                if bdinput[i, j] == 2:
                    A[i][j] = "O"
        for line in A[:][::-1]:
            print(line)

    def run_game():
        board = np.zeros([3, 3], dtype=int)
        player1_retry = 0
        player2_retry = 0
        print("The board is setup like this:\n[7] [8] [9]\n[4] [5] [6]\n[1] [2] [3]\n")
        winner = 0
        while winner == 0:
            if player2_retry != 1:
                choice = int(
                    input("PLAYER 1: where would you like to go?\nEnter a number:"))
                if board[((choice - 1) // 3), ((choice % 3) - 1)]:
                    player1_retry = 1
                    print('that spot was already used, try again')
                else:
                    board[((choice - 1) // 3), ((choice % 3) - 1)] = 1
                    player1_retry = 0

            print_board(board)
            winner = check_for_gameover(board)
            if winner != 0:
                break

            if player1_retry != 1:
                choice = int(
                    input("PLAYER 2: where would you like to go?\nEnter a number:"))
                if board[((choice - 1) // 3), ((choice % 3) - 1)]:
                    player2_retry = 1
                    print('that spot was already used, try again')
                else:
                    board[((choice - 1) // 3), ((choice % 3) - 1)] = 2
                    player2_retry = 0

            winner = check_for_gameover(board)
            print_board(board)

    run_game()

if __name__ == '__main__':
    main()