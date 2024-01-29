from TicTacToe import TicTacToe
from Bot import Bot

def main():
    game = TicTacToe()
    while True:
        if game.returnPlayer() == 'X':
            # bot plays
            move = Bot.bestMove(game.returnBoard())
            game.botPlaceValue(move[0], move[1])
        else:
            # player plays
            game.printBoard()
            game.placeValue()
    
        if game.checkWin() != None:
            game.printBoard()
            game.announceWinner()
        else:
            game.updateTurn()

if __name__ == '__main__':
    main()
    