from Bot import Bot

def main ():
    print(_valid_moves())

def _valid_moves():
    board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', ' ', 'X']]
    bot = Bot()
    return bot.valid_moves(board)

if __name__ == '__main__':
    main()