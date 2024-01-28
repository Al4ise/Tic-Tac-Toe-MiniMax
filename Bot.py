class Bot():
    def valid_moves(self, board):
        valid = []
        # add all empty spaces to valid moves
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ' ':
                    valid.append([row, col])
        return valid

    def scoreInterpreter(self, score):
        if score == 'X':
            return 1
        elif score == 'O':
            return -1
        else:
            return 0

    def minimax(self, board, depth, isMax):
        score = self.scoreInterpreter(self, self.checkWin(self, board))

        # if maximizer on minimizer has won, return their score
        if score == 1 or score == -1:
            return score
        
        # if there are no more moves, return 0
        if len(self.valid_moves(self, board)) == 0:
            return 0
        
        # maximizer's move
        if isMax:
            best = -1000
            for move in self.valid_moves(self, board):
                board[move[0]][move[1]] = 'X'
                best = max(best, self.minimax(self, board, depth + 1, not isMax))
                board[move[0]][move[1]] = ' '
            return best
        
        # minimizer's move
        else:
            best = 1000
            for move in self.valid_moves(self, board):
                board[move[0]][move[1]] = 'O'
                best = min(best, self.minimax(self, board, depth + 1, not isMax))
                board[move[0]][move[1]] = ' '
            return best

    @classmethod
    def bestMove (self, board):
        bestVal = -1000
        bestMove = [-1, -1]
        for move in self.valid_moves(self, board):
            board[move[0]][move[1]] = 'X'
            moveVal = self.minimax(self, board, 0, False)
            board[move[0]][move[1]] = ' '
            if moveVal > bestVal:
                bestMove = move
                bestVal = moveVal
        return bestMove

    def checkWin(self, board):
        status=1
        n = len(board)

        # Check Rows
        for row in board:
            # check if all values in row are equal
            if all(element == row[0] for element in row) and row[0] != ' ':
                return row[0]
    
        # Check Columns
        for col in range(n):
            tempvalue = board[0][col]
            if tempvalue == ' ': break
            for row in range(n):
                if board[row][col] != tempvalue:
                    # Column does not have equal values
                    break
            else:
                return tempvalue
        
        # Check diagonals
        tempvalue = board[0][0]
        if tempvalue != ' ':
            for i in range(n):
                if board[i][i] != tempvalue:
                    # Diagonal does not have equal values
                    break
            else:
                # All elements in the diagonal are equal
                return tempvalue

        # Check anti-diagonals
        tempvalue = board[0][n-1]
        if tempvalue != ' ':
            for i in range(n):
                if board[i][n-i-1] != tempvalue:
                    # Anti-diagonal does not have equal values
                    break
            else:
                # All elements in the anti-diagonal are equal
                return tempvalue
        
        # Check if board is full
        blank_exists = False
        for row in board:
            for col in row:
                if col == ' ':
                    blank_exists = True
                    break
        
        if not blank_exists:
            status = 2 
             
        if status == 1:
            return None 
        else:
            return 'D'  
    
    if __name__ == '__main__':
        #main()
        ...