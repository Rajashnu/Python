import random
import os.path
import json
random.seed()

def draw_board(board):
    """This function takes a 3x3 game board as input and displays it """
    print("---------")
    for i in range(3):
        row = "|"
        for j in range(3):
            row += "" + board[i][j] + "|"
        print(row)
        print("-----------")


def welcome(board):
   """This function displays a welcome message and the state of the game board """
   print("Welcome to Tic-Tac-Toe!\nHere's the current board:")
   draw_board(board)
   print("When prompted, Enter the number of the cell where you'd like to place your symbol:")

def initialise_board(board):
    """This function initializes the game board with empty spaces"""
    for row in range(3):
        for col in range(3):
            board[row][col] = ' ' #initialize each cell to an empty string

    return board
    
def get_player_move(board):
    """This function prompts the player to choose a cell and returns its position as a tuple"""
    while True:
        player_move = input(" 1 2 3 \n 4 5 6 \n 7 8 9 \n choose your square:")
        if player_move in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            player_move = int(player_move) - 1
            row, col = int(player_move / 3), player_move % 3
            if board[row][col] == ' ':
                return row, col
            print("This cell is already occupied. Please choose a different cell.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

        return row, col

def choose_computer_move(board):
    """This function chooses an empty cell for the computer and returns it as tuple"""
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return row, col
    return row, col


def check_for_win(board, mark):
      """This function determines the win or loss of the player"""
      if (board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or \
        (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or \
        (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or \
        (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or \
        (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or \
        (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or \
        (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or \
            (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark):
          return True
      return False

def check_for_draw(board):
    """This function checks if the game has resulted into a draw"""
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    return True
        
def play_game(board):
    """This function implements a game of tic-tac-toe"""
    # initialise the board
    initialise_board(board)
    while True:
        player_move = get_player_move(board)
        if player_move is not None:
            board[player_move[0]][player_move[1]] = "X"
            draw_board(board)
            if check_for_win(board, "X"):
                return 1
            if check_for_draw(board):
                return 0
            computer_move = choose_computer_move(board)
            board[computer_move[0]][computer_move[1]] = "O"
            print("Computer made a choice")
            draw_board(board)
            if check_for_win(board, "O"):
                return -1
            if check_for_draw(board):
                return 0
        continue
                    
                
def menu():
   # Loop run continuously until user input valid data (1,2,3,q);
    """The function provides a menu with four options:
        1. Play game
        2. Save score
        3. Leaderboard
        q. Quit """
    while True:
        choice = input("1. Play game\n2. Save score\n3. Leaderboard\nq. Quit\nEnter your choice: ")
        # check if choice is a valid data which is (1 to play game, 2, 3, q);
        if choice in ['1', '2', '3', 'q']:
            # if choice is valid it is returned.
            return choice
        # if choice is not valid loop run continuously.
        print("Invalid input. Please enter a valid choice (1, 2, 3, q).")
        return choice

def load_scores():
   """Load the leaderboard data from a file. If the file does not exist, creates a new file"""
   try:
        # Open the file in read mode
        with open("leaderboard.txt", "r") as file:
            leaderboard = json.load(file)
   except FileNotFoundError:
        # if the file doesn't exist, Create a new directory
        leaderboard = {}
   return leaderboard
    
def save_score(score):
    """Saves the score of a player to the leaderboard in a txt file"""
    player_name = input("Enter your name: ")
    try:
        with open("leaderboard.txt", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    data[player_name] = score
    with open("leaderboard.txt", "w") as file:
        json.dump(data, file)
    


def display_leaderboard(leaders):
    """Dispalys the leaderboard by printing the name and score of players"""
    print("Leaders:")
    for name, score in leaders.items():
        print(f"{name}: {score}")

def main():
    board = [ ['1','2','3'],\
              ['4','5','6'],\
              ['7','8','9']]

    welcome(board)
    total_score = 0
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:',total_score)
        if choice == '2':
            save_score(total_score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return


    
# Program execution begins here
if __name__ == '__main__':
    main()
