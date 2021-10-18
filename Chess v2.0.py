#Problem: A knight piece is randomly placed on a chessboard.
#The knight moves in a random direction until it falls off the board.
#Count the number of moves the knight makes over 1000 tests and find the average number of moves to fall off the board.

#Assumed steps to solve the problem:
#import random function
import random
from random import seed
from random import randint
seed() #Sets the random seed.  Use defined value for testing otherwise leave blank.

# #8 x 8 board can be represented in an x,y grid system counting from 0 to 7
# #Knight starts in a random location using the randint function

#Knight moves in a random move using one of: (2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)
knight_move = ((2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2))
number_runs = 1000#Set to however many runs you want to do.
total = 0

for moves in range(number_runs):
    # 8 x 8 board can be represented in an x,y grid system counting from 0 to 7
    x = randint(0, 7)
    y = randint(0, 7)
    moves = 0
    for runs in range(100):  #Would work better to use something until failure instead of a range.

        # Print starting point for testing.
        print("Starting x= ", x)
        print("Starting y= ", y)

        # Knight starts in a random location using the randint function
        knight_choice = random.choice(knight_move)
        print("Knight move= ",knight_choice)
        # list.append(moves+1)
    #Create an if statement to check x and y against initial parameters x,y > 7 or x,y < 0; else add the knight_choice
        if x > 7:

            print("Failed at move= ", moves+1)
            print("")
            total = total + moves + 1
            break
        elif y > 7:

            print("Failed at move= ", moves+1)
            print("")
            total = total + moves + 1
            break
        elif x < 0:

            print("Failed at move= ", moves+1)
            print("")
            total = total + moves + 1
            break
        elif y < 0:

            print("Failed at move= ", moves+1)
            print("")
            total = total + moves + 1
            break
        else:

            x = x + knight_choice[0]
            y = y + knight_choice[1]

        # Add 1 to moves if it doesn't fail
        moves = moves + 1

#Count the number of Knight moves on each run until it moves outside of the board grid
#Run the tests 1000 times tracking the number of moves to fall outside on each run (or maybe a running total?)
#Average the number of moves from all the tests
print("Total: ", total)
print("Average Number of moves: ",float(total/number_runs))



