import os
class TicTacToe:
    def __init__(self, n=3, m=3):
        # Create the board (A nxn matrix, default is 3x3)
        self.board = [[' ' for _ in range(n)] for _ in range(n)]
        self._m=m
        self._player = 'X'
    
    def printBoard(self):
        # Print the board
        for row in self.board:
            print('|', end='')
            for col in row:
                print(col, '|', end='')
            print()
    
    def placeValue(self):
        # Place a value on the board
        while True:
            row = int(input('Enter Row: '))
            col = int(input('Enter Column: '))
            if self.validMove(row, col):
                self.board[row][col] = self._player
                break
            else:
                print('Invalid Move')
            
    def botPlaceValue(self, row=-1, col=-1):
        # Place a value on the board
        while True:
            if self.validMove(row, col):
                self.board[row][col] = self._player
                break
            else:
                print('Invalid Move')
                break
            
    def returnBoard (self):
        return self.board
    
    def returnPlayer (self):
        return self._player

    def validMove(self, row, col):
        if (0 <= row < len(self.board)) and (0 <= col < len(self.board)):
            if self.board[row][col] == ' ':
                return True
        
        return False
    
    def updateTurn(self):
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

    def checkWin(self, board=None):
        if board == None:
            board = self.board
        
        # Check Rows
        for row in board:
            # check if all values in row are equal
            if all(element == row[0] for element in row) and row[0] != ' ':
                return row[0]

        # Check Columns
        for col in range(len(board)):
            tempvalue = board[0][col]
            if tempvalue == ' ': break
            for row in range(len(board)):
                if board[row][col] != tempvalue:
                    # Column does not have equal values
                    break
            else:
                return tempvalue
        
        # Check diagonals
        tempvalue = board[0][0]
        if tempvalue != ' ':
            for i in range(len(board)):
                if board[i][i] != tempvalue:
                    # Diagonal does not have equal values
                    break
            else:
                # All elements in the diagonal are equal
                return tempvalue

        # Check anti-diagonals
        tempvalue = board[0][len(board)-1]
        if tempvalue != ' ':
            for i in range(len(board)):
                if board[i][len(board)-i-1] != tempvalue:
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
        
        if blank_exists: # Game is still on
             return None
        else: # Game is a draw
            return 'D'

    def announceWinner (self):
        winner = self.checkWin()
        if winner == 'D':
            print('Game is a Draw')
        else:
            print(f'{winner} has won the game')
            
#if __name__ == '__main__':
#    main()