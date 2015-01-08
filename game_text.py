# AQA Computer Science practice game scenario
# Snakes and Ladders
# by P Dring

""" imports """
import random

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
    # display main menu
    print "1: Change player 1's name"
    print "2: Change player 2's name"
    print "3: Play game"
    print "Q: Quit"
    
    # blank line
    print
    choice = raw_input("Please choose 1,2,3 or Q:")
    return choice

""" Task 2 """
# procedure that changes a player's name
# player_number is a integer between 1 and 2
def change_name(player_number):
    # display current player number
    current_name = names[player_number - 1]
    print "Player " + str(player_number) + "'s name is currently: ", current_name
    
    # ask user for new name
    new_name = raw_input("Please type new name (or leave blank to keep current):")
    
    # if user leaves the name blank, don't change the name
    if new_name == "":
        new_name = current_name
    
    # save the new name
    names[player_number - 1] = new_name
    
""" Task 3 """
# displays the game board
def display_board():
    # just display the text
    print """
.   .   .   .   .   .   .   .   .
 64  63| 62= 61  60  59  58  57
.   .  |.  =.   .   .   .   .   .
 49  50| 51= 52  53  54  55| 56
.   .  |.  =.   .   .   .  |.   .
 48  47| 46= 45  44= 43  42| 41
.   .   .  =.   .   =   .  |.   .
 33  34  35= 36  37 =38  39| 40
.   .   .   =   .   .== .  |.  =.
 32  31  30 =29  28  27= 26| 25=
.   .   .   =   .   .   .   .== .
 17  18  19 =20  21  22  23 =24
.   .   .   .   .   .   .  ==   .
 16  15  14  13  12  11  10== 9
.   .   .   .   .   .   .  ==   .
  1   2   3   4   5   6   7=  8
.   .   .   .   .   .   .   .   .
    """
    print names[0], "is on square: ", pos[0]
    print names[1], "is on square: ", pos[1]
    print

""" Task 4 """
# function that rolls a die for either player 1 or player 2
# player: integer (0 or 1)
# returns integer: the die number thrown (1-6)
def roll_die(player):
    # choose random number between 1 and 6
    roll = random.randint(1,6)
    print names[player] + "'s go:"
    raw_input("Press Enter to continue")
    
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
    print names[player], "has rolled a", roll
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
    raw_input("Press Enter to continue")
    
    
    # return result of die throw
    return roll
    
# procedure to let player 1 then player 2 throw a die
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
    while True:
        take_turn()        

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
