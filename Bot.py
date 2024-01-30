from TicTacToe import TicTacToe
class Bot(TicTacToe):
    @classmethod
    def validMoves(cls, board):
        valid = []
        # add all empty spaces to valid moves
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ' ':
                    valid.append([row, col])
        return valid

    @classmethod
    def scoreInterpreter(cls, score):
        if score == 'X':
            return 1
        elif score == 'O':
            return -1
        else:
            return 0

    @classmethod
    def checkWin(cls, board):
        return cls._checkWin(board)
    
    @classmethod
    def minimax(cls, board, depth, isMax):
        score = cls.scoreInterpreter(cls.checkWin(board))

        # if maximizer on minimizer has won, return their score
        if score == 1 or score == -1:
            return score
        
        # if there are no more moves, return 0
        if len(cls.validMoves(board)) == 0:
            return 0
        
        # maximizer's move
        if isMax:
            best = -1000
            for move in cls.validMoves(board):
                board[move[0]][move[1]] = 'X'
                best = max(best, cls.minimax(board, depth + 1, not isMax))
                board[move[0]][move[1]] = ' '
            return best
        
        # minimizer's move
        else:
            best = 1000
            for move in cls.validMoves(board):
                board[move[0]][move[1]] = 'O'
                best = min(best, cls.minimax(board, depth + 1, not isMax))
                board[move[0]][move[1]] = ' '
            return best

    @classmethod
    def bestMove(cls, board):
        bestVal = -1000
        bestMove = [-1, -1]
        for move in cls.validMoves(board):
            board[move[0]][move[1]] = 'X'
            moveVal = cls.minimax(board, 0, False)
            board[move[0]][move[1]] = ' '
            if moveVal > bestVal:
                bestMove = move
                bestVal = moveVal
        return bestMove
    
    if __name__ == '__main__':
        #main()
        ...