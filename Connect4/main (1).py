

""" Starter code for an interactive, text-based Connect 4 game.
Emma and Hadi 
21/04/2022

@author: Brian Law
"""
from __future__ import annotations

class Board:
  """ Starter code for the Connect 4 board. """

  def __init__(self) -> None:
    """ This uses empty lists to create spaces in the board"""
    # We did 6 lists of 7 empty spaces all in a list to create the spaces. 
    self.board = [[' ', ' ',' ',' ',' ',' ',' '],[' ', ' ',' ',' ',' ',' ',' '], [' ', ' ', ' ',' ',' ',' ',' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '] , [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

  def output_board(self) -> None:
    """ Outputs the current Connect 4 board to the console. """
    
    
    print('===============================')
    for row_num in range(len(self.board)):
      row_str = '|'
      for col_num in range(len(self.board[row_num])):
        row_str += '| ' + self.board[row_num][col_num] + ' '
      row_str += '||'
      print(row_str)
      if row_num < len(self.board) - 1:   
        print('-------------------------------')
    print('===============================')

  def play_piece(self, column: int, piece: str) -> bool:
    """This method will take a piece and put it into a position on the board given the column number. It will return false if all the spaces are empty. It will return true if the piece is able to be played. 
    :param column: This parameter takes in the number of the column 
    :param piece: This parameter tkes in the pece which will be a "O" or an "x"
    Return: Will return false if all spaces are filled or will return true if the piece is able to be played. 
    """
    #Here is the loop of the columns checking all of the them. 
    for i in range(5,-1,-1):
      
      
      #Here is the if statement saying if the columns are all full it will return false. 
      if self.board[0][column-1] != " ":
        return False
        # Elif statement saying if te piece is able to be played in the empty spot it will return true. 
      elif self.board[i][column-1] == " ":
          self.board[i][column-1] = piece
          return True
      
        
    
    
             
  

  def is_full(self) -> bool:
    
    """ checks to see if the board is full or not and returns 
    True or False depending on it
    :return: True or False depending if it is full or not"""
    # This checks all of the columns of the board in a loop.
    for i in range(5,-1,-1):
      #This checks all of the rows in the board in a loop 
      for j in range(6, -1, -1):

        #This says that if the whole board is empty in which it will return false and if the whole board is full it will return true.
        if self.board[i][j] == " ":
          return False
    return True

      
      
    #Your code goes here
    pass

  def check_victor(self) -> str:
    
    
    """uses check_victor_h, check_victor_v and check_victor_d to check which peice one
    :return: The peice that one or empty string if no player """
    
    #Here we are giong through every option for horizontal, vertical and diagonal and if the returns are X or Y it will return as such and if there is no answer it will return an empty string. 
    if self.check_victor_h() == 'X':
      return 'X'
    elif self.check_victor_h() == 'O':
      return 'O'
    elif self.check_victor_v() == 'O':
      return 'O'
    elif self.check_victor_v() == "X":
      return 'X'
    elif self.check_victor_d() == "X":
      return "X"
    elif self.check_victor_d() == "O":
      return "O"
    else:
      return " "
  
    

  def check_victor_h(self) -> str:
    """checks to see if there are four in a row of a peice 
    horizontally 
    :return: the peice that 'won' or an empty string otherwise"""
    
    
    # loop to go over each column
    for j in range(5,-1,-1):
      
      # accumulator in the loop to count O's and X's
      # reset everytime the loop is run
      accumulator_o = 0
      accumulator_x = 0

      # loop over each row
      for i in range(6, -1, -1):

        # if statements to check each condition
        # add to accumulator everytime O or X 
        if self.board[j][i] == 'O':
          accumulator_o = accumulator_o + 1
          accumulator_x = 0
        elif self.board[j][i] == 'X':
          accumulator_x = accumulator_x + 1
          accumulator_o = 0
        if accumulator_o >= 4:
          return 'O'
        elif accumulator_x >= 4:
          return 'X'

    # if statement to return empty string if win conditions not met
    if accumulator_o < 4 and accumulator_x < 4:
      return " "
    return " "

        

  def check_victor_v(self) -> str:
    """checks to see if there """
    # Same thing as the horizontal for the same reasons.
    for i in range(7):
     
       accumulator_o = 0
       accumulator_x = 0
    
       for j in range(6):
     
        if self.board[j][i] == 'O':
          accumulator_o = accumulator_o + 1
          accumulator_x = 0
        elif self.board[j][i] == 'X':
          accumulator_x = accumulator_x + 1
          accumulator_o = 0
        if accumulator_o >= 4:
          return 'O'  
        elif accumulator_x >= 4:
          return 'X'
       if accumulator_o<4 and accumulator_x < 4:
          return " "
    

  def check_victor_d(self) -> str:
    """checks to see if there was a winner diagonally
    :return: the peice that won or blank otherwise"""
      
        
     
      
      # all possible combinations of winning diagonally
    combo1 = [self.board[2][0],self.board[3][1],self.board[4][2],self.board[5][3]]   
    combo2 = [self.board[1][0],self.board[2][1],self.board[3][2],self.board[4][3]]
    combo3 = [self.board[2][1], self.board[3][2],self.board[4][3],self.board[5][4]]
    combo4 = [self.board[0][0], self.board[1][1],self.board[2][2],self.board[3][3]]
    combo5 = [self.board[1][1], self.board[2][2],self.board[3][3], self.board[4][4]]
    combo6 = [self.board[2][2], self.board[3][3],self.board[4][4], self.board[5][5]]
    combo7 = [self.board[0][1], self.board[1][2],self.board[2][3], self.board[3][4]]
    combo8 = [self.board[1][2], self.board[2][3], self.board[3][4],self.board[4][5]]
    combo9 = [self.board[2][3],self.board[3][4],self.board[4][5], self.board[5][6]]                   
    combo10 = [self.board[0][2],self.board[1][3],self.board[2][4], self.board[3][5]]
    combo11 = [self.board[1][3],self.board[2][4], self.board[3][5],self.board[4][6]]
    combo12 = [self.board[0][3], self.board[1][4], self.board[2][5], self.board[3][6]]       
    combo13 = [self.board[2][6], self.board[3][5],self.board[4][4], self.board[5][3]]
    combo14 = [self.board[1][6], self.board[2][5], self.board[3][4], self.board[4][3]]
    combo15 = [self.board[2][5], self.board[3][4], self.board[4][3], self.board[5][2]]              
    combo16 = [self.board[0][6],self.board[1][5],self.board[2][4], self.board[3][3]]
    combo17 = [self.board[1][5],self.board[2][4],self.board[3][3], self.board[4][2]]
    combo18 = [self.board[2][4],self.board[3][3],self.board[4][2],self.board[5][1]]     
    combo19 = [self.board[0][5],self.board[1][4], self.board[2][3], self.board[3][2]]
    combo20 = [self.board[1][4],self.board[2][3],self.board[3][2], self.board[4][1]]     
    combo21 = [self.board[2][3],self.board[3][2],self.board[4][1], self.board[5][0]]
    combo22 = [self.board[0][4],self.board[1][3], self.board[2][2], self.board[3][1]]       
    combo23 = [self.board[1][3],self.board[2][2],self.board[3][1],self.board[4][0]]     
    combo24 = [self.board[0][3],self.board[1][2],self.board[2][1], self.board[3][0]]
  
    
    # winner combinations list to check with in the loop
    all_combos = [combo1, combo2, combo2, combo3, combo4, combo5, combo6,combo7, combo8, combo9, combo10, combo11, combo12, combo13, combo14, combo15, combo16, combo17, combo18, combo19, combo20, combo21, combo22, combo23, combo24]
    
    #This loop goes over the length of all the combos and if it sees 4 xs it will return x since that is the answer and the same thing goes for O
    found = False
    for x in all_combos:
   
  
      if x == ["X","X","X","X"]:
        found = True
        return "X"
        break
        
      if x == ["O","O","O","O"]:
        found = True
        return "O"
        break
  
    if found == False:
      return " "
      
       
  


      
    
      
        
  


def play_game():
  """ Here we are actually playing the game. The players input a column number and a string and it repeats until osmeone has won or the board is full"""
  print('Welcome to CS127 Connect 4!')
  board = Board()
  board.output_board()
  #This is saying that while the board is not full it should ask the players to input column and string. 
  while board.is_full()  == False:
    user_input1 = int(input('enter a column number 1-7: '))
    user_input2 = input('please enter a piece from O or X: ')

    # checks wheather or not there is a valid input
    if (board.play_piece(user_input1, user_input2))==True:
      board.output_board()
    else:
      print("Incorrect input, please try another input.")

    # variable to check for check victor 
    var = board.check_victor()

    # if statement to see if it is not blank, then print the peice
    # that won
    if var!=" ":
      print("The winner is: ",board.check_victor())
      break

  # end game if no winner if board becomes full 
  if board.is_full()==True:
    print("No winner, game has ended.")
  else:
    print("Game End. Thank you for playing!")
 

'''
  board.play_piece(1,"X")
  board.play_piece(1, "X")
  board.play_piece(1,"X")
  board.play_piece(1,"X")
  board.play_piece(1,"X")
  board.play_piece(1,"X")
  board.play_piece(1,"X")
  board.play_piece(1,"X")
  
  board.output_board()
'''
  # Victory tests
  
board = Board()
"""
board.play_piece(1, 'X')
board.play_piece(1, 'X')
board.play_piece(1, 'X')
board.play_piece(1, 'X')
board.output_board()
print(board.check_victor_v())
print(board.check_victor())
"""
"""
board.play_piece(7, 'X')
board.play_piece(7, 'X')
board.play_piece(7, 'X')
board.play_piece(7, 'X')
board.output_board()
print(board.check_victor_v())
print(board.check_victor())
"""

"""
  board.play_piece(1, 'O')
  board.play_piece(2, 'O')
  board.play_piece(3, 'O')
  board.play_piece(4, 'O')
  board.output_board()
  print(board.check_victor_h())
"""
"""
  board.play_piece(4, 'X')
  board.play_piece(5, 'X')
  board.play_piece(6, 'X')
  board.play_piece(7, 'O')
  board.play_piece(4, 'O')
  board.play_piece(5, 'O')
  board.play_piece(6, 'O')
  board.play_piece(7, 'O')
  board.output_board()
  print(board.check_victor())
"""
"""
  board.play_piece(2, 'X')
  board.play_piece(3, 'X')
  board.play_piece(3, 'X')
  board.play_piece(4, 'X')
  board.play_piece(4, 'X')
  board.play_piece(4, 'X')
  board.play_piece(1, 'O')
  board.play_piece(2, 'O')
  board.play_piece(3, 'O')
  board.play_piece(4, 'O')
  board.output_board()
  print(board.check_victor_d())
"""
'''
  board.play_piece(4, 'X')
  board.play_piece(4, 'X')
  board.play_piece(4, 'X')
  board.play_piece(5, 'X')
  board.play_piece(5, 'X')
  board.play_piece(6, 'X')
  board.play_piece(4, 'O')
  board.play_piece(5, 'O')
  board.play_piece(6, 'O')
  board.play_piece(7, 'O')
  board.output_board()
  print(board.check_victor())
'''

  # No victory tests
"""
  board.play_piece(1, 'O')
  board.play_piece(1, 'X')
  board.play_piece(1, 'O')
  board.play_piece(1, 'X')
  board.play_piece(1, 'O')
  board.play_piece(1, 'O')
  board.play_piece(1, 'O')
  board.play_piece(1, 'O')
  board.output_board()
  print(board.check_victor())
"""
"""
  board.play_piece(7, 'X')
  board.play_piece(7, 'O')
  board.play_piece(7, 'X')
  board.play_piece(7, 'O')
  board.play_piece(7, 'X')
  board.play_piece(7, 'X')
  board.play_piece(7, 'X')
  board.play_piece(7, 'X')
  board.output_board()
  print(board.check_victor())
"""
"""
board.play_piece(1, 'X')
board.play_piece(2, 'X')
board.play_piece(3, 'X')
board.play_piece(7, 'X')
board.output_board()
print(board.check_victor())
"""
"""
board.play_piece(5, 'X')
board.play_piece(6, 'X')
board.play_piece(7, 'X')
board.play_piece(1, 'O')
board.play_piece(5, 'O')
board.play_piece(6, 'O')
board.play_piece(7, 'O')
board.play_piece(1, 'O')
board.output_board()
print(board.check_victor())
"""
"""
  board.play_piece(1, 'X')
  board.play_piece(2, 'X')
  board.play_piece(2, 'X')
  board.play_piece(3, 'X')
  board.play_piece(3, 'X')
  board.play_piece(3, 'X')
  board.play_piece(7, 'O')
  board.play_piece(1, 'O')
  board.play_piece(2, 'O')
  board.play_piece(3, 'O')
  board.output_board()
  print(board.check_victor())
"""
"""
  board.play_piece(5, 'X')
  board.play_piece(5, 'X')
  board.play_piece(5, 'X')
  board.play_piece(6, 'X')
  board.play_piece(6, 'X')
  board.play_piece(7, 'X')
  board.play_piece(5, 'O')
  board.play_piece(6, 'O')
  board.play_piece(7, 'O')
  board.play_piece(1, 'O')
  board.output_board()
  print(board.check_victor())
"""

play_game()