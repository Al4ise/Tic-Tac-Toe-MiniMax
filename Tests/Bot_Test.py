from Bot import Bot

def main ():
    #print(_valid_moves())
    print(_minimax())

def _valid_moves():
    board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', ' ', 'X']]
    bot = Bot()
    return bot.valid_moves(board)

def _minimax():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], ['X', ' ', ' ']]
    bot = Bot()
    return bot.minimax(board, 0, True)

if __name__ == '__main__':
    main()