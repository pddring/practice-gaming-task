# AQA Computer Science practice game scenario
# Snakes and Ladders
# by P Dring


""" imports """
import random
from pygame_helper import *

""" Global variables """
    
# player names
names = ["Player 1", "Player 2"]

# number of turns each player has had
turns = [0,0]

# player positions
pos = [1,1]

# number of times each number has been rolled for each player
rolls = [{1:0, 2:0, 3:0, 4:0, 5:0, 6:0},
         {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}]

# snake positions
snakes_top =    [18, 63, 55]
snakes_bottom = [5,  47, 26]

# ladder position
ladders_bottom = [7,  27, 20]
ladders_top =    [40, 44, 62]

        

""" Task 1: Main Menu """
# function that displays main menu and returns the user's choice
def main_menu():
    # wipe screen
    screen.fill((255,255,255))
    
    # display main menu
    print_at(screen, (0,0), "Main menu", 20, (0,0,0))
    print_at(screen, (0,20), "1: Change player 1's name", 20, (0,0,0))
    print_at(screen, (0,40), "2: Change player 2's name", 20, (0,0,0))
    print_at(screen, (0,60), "3: Play game", 20, (0,0,0))
    print_at(screen, (0,80), "Q: Quit", 20, (0,0,0))
    pygame.display.flip()
    
    choice = raw_input_at(screen, (0, 100), (0, 120, 200, 20), "Please choose 1,2,3 or Q:", 20, (255,0,0))
    return choice

""" Task 2 """
# procedure that changes a player's name
# player_number is a integer between 1 and 2
def change_name(player_number):
    screen.fill((255,255,255))
    # display current player number
    current_name = names[player_number - 1]
    print_at(screen, (0,0), "Player " + str(player_number) + "'s name is currently: " + current_name, 20, (0,0,0)) 
    
    # ask user for new name
    new_name = raw_input_at(screen, (0, 20), (0,40,100,20), "Please type new name (or leave blank to keep current):", 20, (255,0,0))
    
    # if user leaves the name blank, don't change the name
    if new_name == "":
        new_name = current_name
    
    # save the new name
    names[player_number - 1] = new_name

# convert a square number to x and y grid coordinates
# square_number is an integer between 1 and 64
# returns x,y where x and y are both integers between 0 and 7
def get_coordinates(square_number):
    square_number -= 1
    
    # y is the row if the grid
    y = 7 - int(square_number / 8)
    
    # x is the column of the grid
    x = 7 - (square_number % 8)
    
    # if y s an odd number, the x numbers count from right to left
    if y % 2 == 1:
        x = 7 - x
        
    # return both coordinates
    return x,y 

""" Task 3 """
# display the game board
def display_board():
    font = pygame.font.Font(None, 24)
    black = (0,0,0)
    white = (255,255,255)
    screen.fill(white)
    
    SQUARE_SIZE = 40
    
    # draw player 2 counter in red
    x,y = get_coordinates(pos[1])
    pygame.draw.rect(screen, (255,0,0), (x * SQUARE_SIZE, y * SQUARE_SIZE, 20, 20))
    
    # draw player 1 counter in blue
    x,y = get_coordinates(pos[0])
    pygame.draw.rect(screen, (0,0,255), (20 + x * SQUARE_SIZE, y * SQUARE_SIZE, 20, 20))
    
    
    # draw each square
    for s in range(1, 65):
        x,y = get_coordinates(s)
        pygame.draw.rect(screen, black, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
        txt = font.render(str(s), True, black)
        screen.blit(txt, (x* SQUARE_SIZE, y * SQUARE_SIZE))
        
    # draw each ladder in brown    
    for i in range(len(ladders_bottom)):
        start_line = get_coordinates(ladders_top[i])        
        end_line = get_coordinates(ladders_bottom[i])
        pygame.draw.line(screen, (100,100,0), 
                         (10 + start_line[0] * SQUARE_SIZE, 10 + start_line[1] * SQUARE_SIZE),
                         (10 + end_line[0] * SQUARE_SIZE, 10 + end_line[1] * SQUARE_SIZE), 8)
        
        
    # draw each snake in green
    for i in range(len(snakes_bottom)):
        start_line = get_coordinates(snakes_top[i])        
        end_line = get_coordinates(snakes_bottom[i])
        pygame.draw.line(screen, (0,255,0), 
                         (10 + start_line[0] * SQUARE_SIZE, 10 + start_line[1] * SQUARE_SIZE),
                         (10 + end_line[0] * SQUARE_SIZE, 10 + end_line[1] * SQUARE_SIZE), 8)
        
    
    
    # display current player positions
    print_at(screen, (0, 350), names[0] + " is on square: " + str(pos[0]), 20, (255,0,0))
    print_at(screen, (0, 370), names[1] + " is on square: " + str(pos[1]), 20, (0,0,255))
    
    # update the display and wait for a key press
    pygame.display.flip()
    wait_for_key()

""" Task 4 """
# function that rolls a die for either player 1 or player 2
# returns the die number thrown
# player is an integer between 0 and 1
# returns a number between 1 and 6
def roll_die(player):
    # choose random number between 1 and 6
    roll = random.randint(1,6)
    pygame.display.set_caption(names[player] + "'s go:")
    
    # record the rolled number
    rolls[player][roll] += 1
    
    # move on player counter
    pos[player] += roll
    
    # make counters bounce back
    if pos[player] > 64:
        pos[player] += 64 - pos[player]
        
    # slide down a snake
    if pos[player] in snakes_top:
        snake = snakes_top.index(pos[player])
        pos[player] = snakes_bottom[snake]
        
    # climb up a ladder
    if pos[player] in ladders_bottom:
        ladder = ladders_bottom.index(pos[player])
        pos[player] = ladders_top[ladder]
    
    # display result
    pygame.display.set_caption(names[player]+ " has rolled a " + str(roll))
    display_board()
    
    # check if player has won
    if pos[player] == 64:
        print "Well done", names[player]
        print "You have won in ", turns[player], "turns"
        print
        number_names = ["", "one(s)", "two(s)", "three(s)", "four(s)", "five(s)", "six(es)"]
        for num in [1,2,3,4,5,6]:
            print "You rolled", rolls[player][num],number_names[num] 
        exit()
    
    
    # return result of die throw
    return roll
    
# procedure to let both players throw a die in turn
def take_turn():
    # roll die for each player in turn
    players = [0,1]
    
    # loop through each player
    for player in players:
        
        # keep looping on this player until they don't roll a 6
        while True:
            
            # record how many turns this player has had
            turns[player] += 1
            
            # roll a die for this player
            roll = roll_die(player)
            if roll != 6:
                break
            
    
""" Task 6 """
def play_game():
    display_board()
    while True:
        take_turn()        

# setup pygame
pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Pygame Example")
screen.fill((255,255,255))
pygame.display.flip()


# loop until user chooses to quit
while True:
    
    # show main menu
    option = main_menu()
    
    # user chooses to quit: break out of loop
    if option =="Q":
        break
    
    # user chooses to change the player name
    elif option == "1":
        change_name(1)
    elif option == "2":
        change_name(2)
        
    # user chooses to play the game
    elif option == "3":
        play_game()
        
        
