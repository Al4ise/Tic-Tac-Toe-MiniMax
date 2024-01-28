class TicTacToe:
    def __init__(self, n=3, m=3):
        # Create the board (A nxn matrix, default is 3x3)
        self.board = [[' ' for _ in range(n)] for _ in range(n)]
        self._n=n
        self._m=m
        self._player = 'X'
    
    def printBoard(self):
        # Print the board
        for row in self.board:
            print('|', end='')
            for col in row:
                print(col, '|', end='')
            print()
    
    def placeValue(self, row=-1, col=-1):
        # Place a value on the board
        status=True
        while status:
            self.printBoard()
            if row == -1: row = int(input('Enter Row: '))-1
            if col == -1: col = col = int(input('Enter Column: '))-1
            if self.validMove(row, col):
                self.board[row][col] = self._player
                status=False
            else:
                print('Invalid Move')
    
    def returnBoard (self):
        return self.board
    
    def returnPlayer (self):
        return self._player

    def validMove(self, row, col):
        if row > self._n or row < 0 or col > self._n or col < 0:
            return False
        elif self.board[row][col] != ' ':
            return False
        else:
            return True
    
    def updateTurn(self):
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

    def checkWin(self):
        status=1
        # Check Rows
        for row in self.board:
            # check if all values in row are equal
            if all(element == row[0] for element in row) and row[0] != ' ':
                return row[0]

        # Check Columns
        for col in range(self._n):
            tempvalue = self.board[0][col]
            if tempvalue == ' ': break
            for row in range(self._n):
                if self.board[row][col] != tempvalue:
                    # Column does not have equal values
                    break
            else:
                return tempvalue
        
        # Check diagonals
        tempvalue = self.board[0][0]
        if tempvalue != ' ':
            for i in range(self._n):
                if self.board[i][i] != tempvalue:
                    # Diagonal does not have equal values
                    break
            else:
                # All elements in the diagonal are equal
                return tempvalue

        # Check anti-diagonals
        tempvalue = self.board[0][self._n-1]
        if tempvalue != ' ':
            for i in range(self._n):
                if self.board[i][self._n-i-1] != tempvalue:
                    # Anti-diagonal does not have equal values
                    break
            else:
                # All elements in the anti-diagonal are equal
                return tempvalue
        
        # Check if board is full
        blank_exists = False
        for row in self.board:
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
    
    def playGame(self):
        while True:
            self.placeValue()
            self.checkWin()
            self.updateTurn()
            
            if self.checkWin() != None:
                self.printBoard()
                return self.checkWin()
            
#if __name__ == '__main__':
#    main()