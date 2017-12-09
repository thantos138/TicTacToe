class TicTacToe:

    def __init__(self):
        self.player = ""
        self.ai = ""
        self.player_turn = False
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.values = [[2, 1, 2], [1, 3, 1], [2, 1, 2]]
        self.winner = "none"
        while True:
            self.player = input("Would you like to be 'X' or 'O'?: ").strip().upper()
            if self.player == "X":
                self.ai = "O"
                break
            elif self.player == "O":
                self.ai = "X"
                break
            print("I'm sorry, I didn't understand the input.")
        while True:
            go_first = input("Would you like to go first? Please enter 'yes' or 'no': ").strip().lower()
            if go_first == "yes" or go_first == "y":
                self.player_turn = True
                break
            elif go_first == "no" or go_first == "n":
                self.player_turn = False
                break
            print("I'm sorry, I didn't understand the input.")
        print("self.player:", self.player, "self.ai:", self.ai)
        self.print_board()
        self.play()
        
    
    def print_board(self):
        print("\nThe current board:\n")
        for row_num in range(len(self.board)):
            for col_num in range(len(self.board[row_num])):
                if col_num == 0:
                    print(" " + self.board[row_num][col_num], end = "")
                else:
                    print(" | " + self.board[row_num][col_num], end = "")
            if row_num != (len(self.board) - 1):
                print("\n---+---+---")
        print("\n")
        
    
    def get_move(self) -> list:
        while True:
            move = input("It's your move: ")
            move = move.split(" ")
            index = 0
            is_valid = True
            for i in range(len(list(move))):
                if move[index] == "":           #remove spaces
                    move.pop(index)
                else:
                    try:                        #break if strings were given
                        move[index] = int(move[index]) - 1
                        if move[index] > 2 or move[index] < 0 or type(move[index]) != int:      #break if move is out of bounds
                            is_valid = False
                            print("I'm sorry, that is an invalid move, please enter two, space separated integers between 1 and 3 inclusive")
                            break
                    except ValueError:
                        is_valid = False
                        print("I'm sorry, that is an invalid move, please enter two, space separated integers between 1 and 3 inclusive")
                        break
                    index += 1
            if len(move) == 2 and is_valid:     #break if move is more than 2 integers
                if self.board[move[0]][move[1]] == " ":     #break if space is taken
                    self.player_turn = False
                    return move                 #return list with two values both between 0 and 2
                else:
                    print("I'm sorry, there is something in that space already")
                    
    def ai_move(self):
        max = 0
        move = [-1, -1]
        mult = False
        self.redefine_values()
        for row_num in range(len(self.values)):
            for col_num in range(self.values[row_num]):
                if self.values[row_num][col_num] > max:
                    max = self.values[row_num][col_num]
                    move = [row_num, col_num]
                    mult = False
                if self.values[row_num][col_num] == max:
                    mult = True
        if not mult:
            return move
        temp_board = list(self.board)
        temp_board[move[0]][move[1]] = self.ai 
        temp_values = list(self.values)
        temp_values[move[0]][move[1]] = 0
        if self.play_test(temp_board, temp_values, move, self.player):
            pass
    

    def play_test(self, board : [[], [], []], values : [[], [], []], move : [], player_moving : str) -> bool:
        pass
        
        
    
    
    def redefine_values(self, board = "", values = ""):
        if board == "":
            board = self.board
        if values == "":
            values = self.values
        for row_num in board:
            for col_num in board[row_num]:
                if board[row_num][col_num] == " ":
                    if board[row_num - 1][col_num - 1] == board[row_num - 2][col_num - 2]:            #UL
                        if board[row_num - 1][col_num - 1] == self.ai:
                            values[row_num][col_num] = 5
                        elif board[row_num - 1][col_num - 1] == self.player:
                            values[row_num][col_num] = 4
                    elif board[row_num + 1][col_num - 1] == board[row_num + 2][col_num - 2]:          #DL
                        if board[row_num + 1][col_num - 1] == self.ai:
                            values[row_num][col_num] = 5
                        elif board[row_num + 1][col_num - 1] == self.player:
                            values[row_num][col_num] = 4
                    elif board[row_num - 1][col_num + 1] == board[row_num - 2][col_num + 2]:          #UR
                        if board[row_num - 1][col_num + 1] == self.ai:
                            values[row_num][col_num] = 5
                        elif board[row_num - 1][col_num + 1] == self.player:
                            values[row_num][col_num] = 4
                    elif board[row_num + 1][col_num + 1] == board[row_num + 2][col_num + 2]:          #DR
                        if board[row_num + 1][col_num + 1] == self.ai:
                            values[row_num][col_num] = 5
                        elif board[row_num + 1][col_num + 1] == self.player:
                            values[row_num][col_num] = 4
                    elif board[row_num][col_num + 1] == board[row_num][col_num + 2]:                  #R
                        if board[row_num][col_num + 1] == self.ai:
                            values[row_num][col_num] = 5
                        elif board[row_num][col_num + 1] == self.player:
                            values[row_num][col_num] = 4
                    elif board[row_num][col_num - 1] == board[row_num][col_num - 2]:                  #L
                        if board[row_num][col_num - 1] == self.ai:
                            values[row_num][col_num] = 5
                        elif board[row_num][col_num - 1] == self.player:
                            values[row_num][col_num] = 4
                    elif board[row_num - 1][col_num] == board[row_num - 2][col_num]:                  #U
                        if board[row_num - 1][col_num] == self.ai:
                            values[row_num][col_num] = 5
                        elif board[row_num - 1][col_num] == self.player:
                            values[row_num][col_num] = 4
                    elif board[row_num + 1][col_num] == board[row_num + 2][col_num]:                  #D
                        if board[row_num + 1][col_num] == self.ai:
                            values[row_num][col_num] = 5
                        elif board[row_num + 1][col_num] == self.player:
                            values[row_num][col_num] = 4
        return values
                              
    def game_over(self) -> str:         #return string of winner, or empty string
        for row_num in self.board:
            for col_num in self.board[row_num]:
                if self.board[row_num][col_num] != " ":
                    if self.checkUL([row_num, col_num]) == 3:
                        return self.board[row_num, col_num]
                    if self.checkDL([row_num, col_num]) == 3:
                        return self.board[row_num, col_num]
                    if self.checkUR([row_num, col_num]) == 3:
                        return self.board[row_num, col_num]
                    if self.checkDR([row_num, col_num]) == 3:
                        return self.board[row_num, col_num]
                    if self.checkR([row_num, col_num]) == 3:
                        return self.board[row_num, col_num]
                    if self.checkL([row_num, col_num]) == 3:
                        return self.board[row_num, col_num]
                    if self.checkU([row_num, col_num]) == 3:
                        return self.board[row_num, col_num]
                    if self.checkD([row_num, col_num]) == 3:
                        return self.board[row_num, col_num]
        return ""
    
    def checkUL(self, index : []):	
        count = 1
        try:
            if self.board[index[0]][index[1]] == self.board[index[0] - 1][index[1] - 1]:
                count += 1
            if self.board[index[0]][index[1]] == self.board[index[0] - 2][index[1] - 2]:
                count += 1
            return count
        except IndexError:
            return 0
    
    def checkDL(self, index : []):
        count = 1
        try:
            if self.board[index[0]][index[1]] == self.board[index[0] + 1][index[1] - 1]:
                count += 1
            if self.board[index[0]][index[1]] == self.board[index[0] + 2][index[1] - 2]:
                count += 1
            return count
        except IndexError:
            return 0
    
    def checkUR(self, index : []):
        count = 1
        try:
            if self.board[index[0]][index[1]] == self.board[index[0] - 1][index[1] + 1]:
                count += 1
            if self.board[index[0]][index[1]] == self.board[index[0] - 2][index[1] + 2]:
                count += 1
            return count
        except IndexError:
            return 0
    
    def checkDR(self, index : []):
        count = 1
        try:
            if self.board[index[0]][index[1]] == self.board[index[0] + 1][index[1] + 1]:
                count += 1
            if self.board[index[0]][index[1]] == self.board[index[0] + 2][index[1] + 2]:
                count += 1
            return count
        except IndexError:
            return 0
    
    def checkR(self, index : []):
        count = 1
        try:
            if self.board[index[0]][index[1]] == self.board[index[0]][index[1] + 1]:
                count += 1
            if self.board[index[0]][index[1]] == self.board[index[0]][index[1] + 2]:
                count += 1
            return count
        except IndexError:
            return 0
    
    def checkL(self, index : []):
        count = 1
        try:
            if self.board[index[0]][index[1]] == self.board[index[0]][index[1] - 1]:
                count += 1
            if self.board[index[0]][index[1]] == self.board[index[0]][index[1] - 2]:
                count += 1
            return count
        except IndexError:
            return 0
    
    def checkU(self, index : []):
        count = 1
        try:
            if self.board[index[0]][index[1]] == self.board[index[0] - 1][index[1]]:
                count += 1
            if self.board[index[0]][index[1]] == self.board[index[0] - 2][index[1]]:
                count += 1
            return count
        except IndexError:
            return 0
    
    def checkD(self, index : []):
        count = 1
        try:
            if self.board[index[0]][index[1]] == self.board[index[0] + 1][index[1] - 1]:
                count += 1
            if self.board[index[0]][index[1]] == self.board[index[0] + 2][index[1] - 2]:
                count += 1
            return count
        except IndexError:
            return 0
        
    def play(self):
        while True:
            if self.player_turn:
                move = self.get_move()
                self.board[move[0]][move[1]] = self.player
                self.values[move[0]][move[1]] = 0
                if self.game_over() == "":
                    self.print_board()
                self.values = self.redefine_values()
            else:
                print("AI is thinking.......")
                self.ai_move()
                self.player_turn = True
            

t = TicTacToe()