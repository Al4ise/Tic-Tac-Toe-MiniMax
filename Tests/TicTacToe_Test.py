from TicTacToe import TicTacToe

def main():
    _validMove()

def _validMove():
    game = TicTacToe()
    if game.validMove(0, 1):
        print('validMove() Test 1: Passed')

if __name__ == '__main__':
    main()