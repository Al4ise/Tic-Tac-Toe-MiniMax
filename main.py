from TicTacToe import TicTacToe
from Bot import Bot

def main():
    game = TicTacToe()
    while True:
        if game.returnPlayer() == 'X':
            # bot plays
            move = Bot.bestMove(game.returnBoard())
            game.placeValue(move[0]+1, move[1]+1)
        else:
            game.placeValue()
        
        game.checkWin()
        game.updateTurn()
    
        if game.checkWin() != None:
            game.printBoard()
            return game.checkWin()


if __name__ == '__main__':
    main()
    