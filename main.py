'''
My inspriation for the project - LeetCode (Valid Sudoku):

import collections
def isValid(board, num, position):
    # default dict creates a basic hashmap/ dictionary
    # We are adding a set because sets can't have any duplicates and neither can a sudoku
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set) # key: (r/3, r/3) --> to break up board into boxes
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0: # if that board value is empty, move on to next iteration
                continue

            if (board[r][c] in rows[r] or # if the current value is in this row
                board[r][c] in cols[c] or # if the current value is in this column
                board[r][c] in squares[(r//3, c//3)] ): # is the current value is in this square
                return False # because that means it's a duplicate
            
            cols[c].add(board[r][c]) # Add that value into the column to update the columns values for the next iteration
            rows[r].add(board[r][c]) # Add that value into the row to update the rows values for the next iteration
            squares[(r//3, c//3)].add(board[r][c]) # Add that value into the square to update the squares values for the next iteration
    return True

'''

# My Project: The Sudoku Solver - Tahasin Shadat
import pygame
pygame.init()


# Unsolved Sudoku boards:
unsolved_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
solved_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

unsolved_boards = [
    [
        [0, 2, 0, 6, 0, 8, 0, 0, 0],
        [5, 8, 0, 0, 0, 9, 7, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [3, 7, 0, 0, 0, 0, 5, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 0, 0, 1, 3],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 9, 8, 0, 0, 0, 3, 6],
        [0, 0, 0, 3, 0, 6, 0, 9, 0],
        'Unsolved'
    ],
    [
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 7, 0],
        [0, 0, 0, 0, 2, 0, 0, 1, 0],
        [0, 4, 0, 6, 0, 0, 0, 0, 3],
        [0, 5, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 7, 0, 0, 6],
        [0, 0, 0, 0, 0, 5, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        'Unsolved'
    ], 
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
        'Unsolved'
    ]
]

# Vizualization
'''
1) Create the unsolved sudoku board
2) when I click a button, call the solve_sudoku function
3) Edit the solve sudoku_function to add some vizualizations

GUI?
1) Make the player be able to play the full sudoku game: make comments + place / edit the board
'''
screen_width = 750
screen_height = 810
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sudoku Solver Vizualization")
font = pygame.font.Font(None, 36)

def drawText(text, text_x, text_y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (text_x, text_y))

def draw_square_with_border(surface, x, y, size, border_size, square_color, border_color):
    # Draw the square
    pygame.draw.rect(surface, square_color, (x, y, size, size))
    # Draw the border 
    pygame.draw.rect(surface, border_color, (x, y, size, size), border_size)

def draw_board(board, position):
    # Draw a row of squares
    square_size = 70
    border_size = 3
    padding = 5
    start_x = 30
    position_y = 30
    square_color = (255, 255, 255)
    gap_size = 10

    for r in range(9):
        for c in range(9):
            if position == (r, c):
                border_color = (0, 255, 0)
            else:
                border_color = square_color

            draw_square_with_border(
                screen, 
                start_x, 
                position_y, 
                square_size, 
                border_size,
                square_color,
                border_color
            )
            
            if board[r][c] == 0:
                drawText('', start_x + 27.5, position_y + 25, 'black')
            else:
                drawText(str(board[r][c]), start_x + 27.5, position_y + 25, 'black')

            if c % 3 == 2:
                start_x += square_size + padding + gap_size 
            else:
                start_x += square_size + padding

        if r % 3 == 2:
            position_y += square_size + padding + gap_size 
        else:
            position_y += square_size + padding
        start_x = 30


# GUI -> will get to later:
def draw_buttons():
    drawText("Sudoku Solver", 775, 30, "white")
    drawText("By: Tahasin Shadat", 750, 60, "white")
    # Draw "Solve" button
    pygame.draw.rect(screen, (0, 255, 0), (775, 110, 150, 50))
    drawText("Solve", 815, 120, "black")

    # Draw "Reset" button
    pygame.draw.rect(screen, (255, 0, 0), (775, 210, 150, 50))
    drawText("Reset", 815, 220, "black")

    # Draw "Clear" button
    pygame.draw.rect(screen, (0, 0, 255), (775, 310, 150, 50))
    drawText("New Board", 815, 320, "black")

def handle_button_click(pos):
    x, y = pos
    # Check if "Solve" button clicked
    if 700 <= x <= 850 and 110 <= y <= 160:
        solve_sudoku(unsolved_board)

    # Check if "Reset" button clicked
    elif 700 <= x <= 850 and 210 <= y <= 260:
        for r in range(9):
            for c in range(9):
                unsolved_board[r][c] = 0

    # Check if "New Board" button clicked
    elif 700 <= x <= 850 and 310 <= y <= 360:
        for r in range(9):
            for c in range(9):
                unsolved_board[r][c] = 0
    

'''
Sudoku Solver Steps:
1) Pick an Empty Square
2) Try all numbers 1-9
3) Find one that fits
4) Repeat with the next cell/square
5) If a rows solution doesn't work: Backtrack
'''

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)        # row & column
    return False

# print(isValid(unsolved_board))

def canPlace(board, num, position):

    current_row = position[0]
    current_col = position[1]

    # Check for duplicates in the row:
    for i in range(9):
        
        if (board[current_row][i] == num     # if there is a duplicate is in the row
            and position[1] != i):           # and its not the number we just placed in that column
            return False                     # Then we can't place it
    
    # Check for duplicates in the column
    for i in range(9):
        if (board[i][current_col] == num     # if there is a duplicate is in the column
            and position[0] != i):           # and its not the number we just placed in that row
            return False                     # Then we can't place it
        
    '''
    Best way I like to explain this and understood this myself was through an example:
    if my position im placing in is (8, 1), that would be the 7th box, or box (2, 0)
    By flat dividng we get -> (8 //3, 1 //3) = (2, 0)

    So now by multiplying our row by 3, our iteration will start from index [6], which corresponds with top of that square
    By adding 3, we get the range 6-8, which is the box's row. 

    Similarily, by multiplying our column by 3, our iteration will start from index [0], which which corresponds with left of that square
    by adding 3, we get a range of 0-2, which completes the box's columns

    Thus our index starts at the top left of the (2, 0) square, and ends at the bottom right of the (2, 0) square, meaning we checked that entire 3x3 square.

    GENIUS!
    '''
    square_row = position[0] // 3 
    square_col = position[1] // 3  

    # check the box for any duplicates
    for r in range(square_row * 3, square_row * 3 + 3):
        for c in range(square_col * 3, square_col * 3 + 3):
            if (board[r][c] == num and (r, c) != position):
                return False
            
    return True


def solve_sudoku(board):
    # Base case: board is full, means it's solved
    if not find_empty(board):
        return True
    else:
        row, col = find_empty(board) # Board is NOT full, so give me an empty position

    for num in range(1, 10): # number between 1-9 (inclusive)
        if canPlace(board, num, (row, col)): # If I can place the numbers 1-9 here, place it
            board[row][col] = num
            draw_board(board, (row, col))  # Draw the updated board
            pygame.display.update()

            if solve_sudoku(board): # I am going to call solve again with the new value added and keep trying until we find a solution
                return True
            
            board[row][col] = 0 # If none of those solutions are valid/ solve the board, backtrack (AKA Reset)
            draw_board(board, (row, col))  # Draw the updated board after backtracking
            pygame.display.update()

    return False

# Console Visualization
def print_board(board):
    for i in range(9):
        if i % 3 == 0:
            print()

        for j in range(9):
            if j % 3 == 0:
                print('   ', end='')

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')

# print_board(unsolved_board)


# Testing
# print('Unsolved Board:')
# print_board(unsolved_board)
# print('Solved Board:')
# solve_sudoku(unsolved_board)
# print_board(unsolved_board)
# if (unsolved_board == solved_board):
#     print(True)

import random
def display_sudoku():
    board_index = 0
    refresh_text = "Press R to load new board"
    running = True
    while running:

        # Closes the application when we click the X on the top right corner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] == True:
            solve_sudoku(unsolved_boards[board_index])
            unsolved_boards[board_index][9] = 'Solved'

        elif key[pygame.K_r] == True:
            if (board_index < 2):
                board_index += 1
            else:
                board_index = 0
        if (unsolved_boards[0][9] == 'Solved' and unsolved_boards[1][9] == 'Solved' and unsolved_boards[2][9] == 'Solved'):
            refresh_text = 'All Boards are now Solved!'
            

        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     handle_button_click(pos)

        draw_board(unsolved_boards[board_index], (-1, -1))
        drawText("Press SPACE to Solve | " + refresh_text, 75, 745, "white")
        drawText("Note: Solver is slowed down to show the solving process", 40, 775, "white")
        pygame.display.update()

    pygame.quit()

    if (unsolved_board == solved_board):
        print('Sudoku is Solved')

display_sudoku()