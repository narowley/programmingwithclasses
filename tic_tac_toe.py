#Week 2 - Tic-tac-toe
#Made by Nathan Rowley

def main():
    #Defining board positions globaly
    global s_1
    global s_2
    global s_3
    global s_4
    global s_5
    global s_6
    global s_7
    global s_8
    global s_9
    global game_end
    global valid_positions
    s_1 = "1"
    s_2 = "2"
    s_3 = "3"
    s_4 = "4"
    s_5 = "5"
    s_6 = "6"
    s_7 = "7"
    s_8 = "8"
    s_9 = "9"
    game_end = False
    #Positions that haven't been taken
    valid_positions = ["1","2","3","4","5","6","7","8","9"]

    print("Welcome to tic-tac-toe!")
    print_board()

    #Loop that verifies after each turn wether the game is done or not
    while True:
        x_turn()
        if game_end:
            break
        o_turn()
        if game_end:
            break
    
    #Prints congrats message based on who won
    if x_won:
        print("Game Over! X won!")
    if o_won:
        print("Game Over! O Won!")
    if cats_game:
        print("Game Over! Tie Game!")
    
    print("Good game!")

def x_turn():
    global s_1
    global s_2
    global s_3
    global s_4
    global s_5
    global s_6
    global s_7
    global s_8
    global s_9
    global valid_positions
    valid_input = False
    #Loops until user puts in a valid input
    while not valid_input:
        x_location = str(input(f"X's turn! Choose a square: {valid_positions}"))
        #Checks to see if valid number
        if x_location in valid_positions:
            #Removes coresponding number with X
            valid_positions.remove(x_location)
            if x_location == "1":
                s_1 = "X"
            elif x_location == "2":
                s_2 = "X"
            elif x_location == "3":
                s_3 = "X"
            elif x_location == "4":
                s_4 = "X"
            elif x_location == "5":
                s_5 = "X"
            elif x_location == "6":
                s_6 = "X"
            elif x_location == "7":
                s_7 = "X"
            elif x_location == "8":
                s_8 = "X"
            elif x_location == "9":
                s_9 = "X"
            valid_input = True
        else:
            print("Please choose a valid sqaure")
    print_board()
    win_check()

def o_turn():
    global s_1
    global s_2
    global s_3
    global s_4
    global s_5
    global s_6
    global s_7
    global s_8
    global s_9
    global valid_positions
    valid_input = False
    #Loops until user puts in a valid input
    while not valid_input:
        #Checks to see if valid number
        o_location = str(input(f"O's turn! Choose a square: {valid_positions}"))
        if o_location in valid_positions:
            #Removes coresponding number with X
            valid_positions.remove(o_location)
            if o_location == "1":
                s_1 = "O"
            elif o_location == "2":
                s_2 = "O"
            elif o_location == "3":
                s_3 = "O"
            elif o_location == "4":
                s_4 = "O"
            elif o_location == "5":
                s_5 = "O"
            elif o_location == "6":
                s_6 = "O"
            elif o_location == "7":
                s_7 = "O"
            elif o_location == "8":
                s_8 = "O"
            elif o_location == "9":
                s_9 = "O"
            valid_input = True
        else:
            print("Please choose a valid sqaure")
    print_board()
    win_check()

def win_check():
    global game_end
    global x_won
    global o_won
    global cats_game
    x_won = False
    o_won = False
    cats_game = False

    if s_1 == "X":
        #X ROW 1 CHECK
        if s_2 == "X":
            if s_3 == "X":
                game_end = True
                x_won = True
        #X COLUMN 1 CHECK
        elif s_4 == "X":
            if s_7 == "X":
                game_end = True
                x_won = True
        #X DIAGONAL TOP LEFT TO BOTTOM RIGHT CHECK
        elif s_5 == "X":
            if s_9 == "X":
                game_end = True
                x_won = True
    if s_1 == "O":
        #O ROW 1 CHECK
        if s_2 == "O":
            if s_3 == "O":
                game_end = True
                o_won = True
        #O COLUMN 1 CHECK
        elif s_4 == "O":
            if s_7 == "O":
                game_end = True
                o_won = True
        #O DIAGONAL TOP LEFT TO BOTTOM RIGHT CHECK
        elif s_5 == "O":
            if s_9 == "O":
                game_end = True
                o_won = True
    if s_5 == "X":
        #X ROW 2 CHECK
        if s_4 == "X":
            if s_6 == "X":
                game_end = True
                x_won = True
        #X COLUMN 2 CHECK
        elif s_2 == "X":
            if s_8 == "X":
                game_end = True
                x_won = True
    if s_5 == "O":
        #O ROW 2 CHECK
        if s_4 == "O":
            if s_6 == "O":
                game_end = True
                o_won = True
        #O COLUMN 2 CHECK
        elif s_2 == "O":
            if s_8 == "O":
                game_end = True
                o_won = True
    if s_9 == "X":
        #X ROW 3 CHECK
        if s_8 == "X":
            if s_7 == "X":
                game_end = True
                x_won = True
        #X COLUMN 3 CHECK
        elif s_6 == "X":
            if s_3 == "X":
                game_end = True
                x_won = True
        #O COLUMN 3 CHECK
    if s_9 == "O":
        #O ROW 3 CHECK
        if s_8 == "O":
            if s_7 == "O":
                game_end = True
                o_won = True
        elif s_6 == "O":
            if s_3 == "O":
                game_end = True
                o_won = True
    if s_7 == "X":
        #X DIAGONAL BOTTOM LEFT TO TOP RIGHT
        if s_5 == "X":
            if s_3 == "X":
                game_end = True
                x_won = True
    if s_7 == "O":
        #O DIAGONAL BOTTOM LEFT TO TOP RIGHT
        if s_5 == "O":
            if s_3 == "O":
                game_end = True
                o_won = True
    if len(valid_positions) == 0:
        game_end = True
        cats_game = True



def print_board():
    print(f"""
    {s_1}|{s_2}|{s_3}
    -----
    {s_4}|{s_5}|{s_6}
    -----
    {s_7}|{s_8}|{s_9}
    """)

if __name__ == "__main__":
    main()