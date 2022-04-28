# Tic tac toe Spencer Bell 26 April 2022
# not sure what i'm doing




win = False

def main():
    board = [i+1 for i in range(9)]
    move = 0

    while move <9:
        print_board(board)
        turn = turn_finder(move)
        spot,player = user_input(turn)
        board = draw_spot(board, spot, player)
        if win_condition(board):
            print(f'Congrats on the dub {player}. You"re my little pogchamp.')
            break
        move += 1
    print('Game Over')
    print(board)

def print_board(board):
    print(f'''

    {board[0]} | {board[1]} | {board[2]}
    --+---+--
    {board[3]} | {board[4]} | {board[5]}
    --+---+--
    {board[6]} | {board[7]} | {board[8]}
    
    
    ''')

def turn_finder(move):
    if move%2 == 0:
        turn = 0
    else:
        turn = 1
    return turn
    
def user_input(turn):
    if turn == 0:
        player = 'X'
    else:
        player = 'O'
    print(f"It's {player}'s turn!")
    spot = input("Select a space to go:(1-9):")
    return spot, player

def draw_spot(board, spot, player):
    
    board[int(spot)-1] = player
    return board

def win_condition(board):
    return (board[3] == board[4] == board[5] or board[0] == board[1] == board[2] or board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[0] == board[4] == board[8] or board[2] == board[4] == board[6])

main()