#!/usr/bin/python3

def who_is_winner(pieces_position_list):


    # Initialize empty board
    board = [[" ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " "]]
    # Define dict to convert move columns to usable indices
    map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}


    # Check for win condition
    def wincheck(currentboard):
        
        # Check for a Horizontal Streak starting at the specified point
        def horcheck(currentboard, column, row):
            space = currentboard[columnnum][rownum]
            # print("Checking for Horizontal streak starting at col", columnnum, " row", rownum, " - ", space)
            for i in range(1,4):
                # print(currentboard[columnnum+i][rownum], '==', space)
                if currentboard[columnnum+i][rownum] != space:
                    return "Draw"
            return space

        # Check for a Vertical Streak starting at the specified point
        def vertcheck(currentboard, column, row):
            space = currentboard[columnnum][rownum]
            # print("Checking for Vertical streak starting at col", columnnum, " row", rownum, " - ", space)
            for i in range(1,4):
                # print(currentboard[columnnum][rownum+i], '==', space)
                if currentboard[columnnum][rownum+i] != space:
                    return "Draw"
            return space

        # Check for a R-Diagonal Streak starting at the specified point
        def rdiagcheck(currentboard, column, row):
            space = currentboard[columnnum][rownum]
            # print("Checking for R-Diagonal streak starting at col", columnnum, " row", rownum, " - ", space)
            for i in range(1,4):
                # print(currentboard[columnnum+i][rownum+i], '==', space)
                if currentboard[columnnum+i][rownum+i] != space:
                    return "Draw"
            return space

        # Check for a L-Diagonal Streak starting at the specified point
        def ldiagcheck(currentboard, column, row):
            space = currentboard[columnnum][rownum]
            # print("Checking for L-Diagonal streak starting at col", columnnum, " row", rownum, " - ", space)
            for i in range(1,4):
                # print(currentboard[columnnum-i][rownum+i], '==', space)
                if currentboard[columnnum-i][rownum+i] != space:
                    return "Draw"
            return space

        # Pass possible start points for horizontal streak to a function dedicated to looking for them
        for columnnum in range(4):
            for rownum in range(len(currentboard[columnnum])):
                if currentboard[columnnum][rownum] != ' ':
                    checkspace = horcheck(currentboard, columnnum, rownum)
                    if checkspace != "Draw":
                        return checkspace

        # Pass possible start points for vertical streak to a function dedicated to looking for them
        for columnnum in range(len(currentboard)):
            for rownum in range(3):
                if currentboard[columnnum][rownum] != ' ':
                    checkspace = vertcheck(currentboard, columnnum, rownum)
                    if checkspace != "Draw":
                        return checkspace

        # Pass possible start points for R-diagonal streak to a function dedicated to looking for them
        for columnnum in range(4):
            for rownum in range(3):
                if currentboard[columnnum][rownum] != ' ':
                    checkspace = rdiagcheck(currentboard, columnnum, rownum)
                    if checkspace != "Draw":
                        return checkspace

        # Pass possible start points for L-Diagonal streak to a function dedicated to looking for them
        for columnnum in range(6, 3, -1):
            for rownum in range(3):
                if currentboard[columnnum][rownum] != ' ':
                    checkspace = ldiagcheck(currentboard, columnnum, rownum)
                    if checkspace != "Draw":
                        return checkspace
    
    # Take current board state and the move being played and return the new board state
    def placepiece(currentboard, column, player):
        for row in range(len(currentboard[column])):
            if currentboard[column][row] == " ":
                currentboard[column][row] = player
                break
        return currentboard

    # Display the board
    def printboard(currentboard):
        for row in range(5, -1, -1):
            print(''.join([column[row] for column in currentboard]))

    # Iterate through each move and check for win condition afterwards
    for move in pieces_position_list:
        # print("\n\nMove: ", move, "\n")

        # Populate board
        board = placepiece(board, map[move[0]], move[2])
        
        # printboard(board)
        
        # Check for a winning move each round.
        winner = wincheck(board)
        if winner == "R":
            return "Red"
        elif winner == "Y":
            return "Yellow"

    # If the game runs out of moves and no one wins, then call it a draw
    return "Draw"

if __name__ == "__main__":
    print(who_is_winner(['F_Red', 'A_Yellow', 'B_Red', 'C_Yellow', 'A_Red', 'E_Yellow', 'C_Red', 'B_Yellow', 'D_Red', 'D_Yellow', 'E_Red', 'B_Yellow', 'C_Red', 'E_Yellow', 'G_Red', 'F_Yellow', 'G_Red', 'E_Yellow', 'D_Red', 'E_Yellow', 'B_Red', 'E_Yellow']))
    print(who_is_winner([ 
        "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
        "D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red", 
        "B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"]))
