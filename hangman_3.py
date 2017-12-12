#Emma #1 
#Start Screen and End Screen
import os
import random
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def show_start_screen():
    start = open('art/start_screen.txt', 'r')
    startgo = start.read()
    print(startgo)   
    print("                                   " + name)
    print(" ")
def instructions(name):
    print("Hello " + name + """. The goal of this game is to guess the word before the Hippo gets away.
 Since we all like hippos please for all of human kinds sake dont let the
 hippo get away.""")
    print(" ")
    print(" ")
    print(" ")
    

    
def end(name):
    print("Thank you for playing, " + name + ". Come back soon! Game made bt Emma #1")
    end = open('art/end_screen.txt', 'r')
    endgo = end.read()
    print(endgo)   

#How the game works
def menu(file_names):
    for i,f in enumerate(file_names):
        print(str(i) + ") " + f[:-4])

    choice = input("Which one?")
    choice = int(choice)

def get_puzzle(file_names, file):
    with open(file, 'r') as f:
        lines = f.read().splitlines()



    category = lines[0]
    puzzle = random.choice(lines[1:])
    
    print(category)
    return(puzzle)
def get_solved(puzzle, guesses):
    solved = ""
    puzzle.lower
    for letter in puzzle:
        if letter in guesses or not letter.isalpha():
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess(guesses):

    while True:
        
        guess = input("Enter a letter: ")
        if len(guess) > 1 :
            print ("Please enter only 1 letter at a time")
        elif guess not in alpha:
            print ("Please enter an actual number.")
        elif guess in guesses:
            print("You already guessed that latter")
        else:
            return guess
    print("")
def display_board(strikes, solved, guesses):
    print("***********")
    print(solved)
    print("***********")

    if strikes == 1:
        one = open('strikes/1.txt', 'r')
        onego = one.read()
        print(onego)
    elif strikes == 2:
        two = open('strikes/2.txt', 'r')
        twogo = two.read()
        print(twogo)
    elif strikes == 3:
        three = open('strikes/3.txt', 'r')
        threego = three.read()
        print(threego)
    elif strikes == 4:
        four = open('strikes/4.txt', 'r')
        fourgo = four.read()
        print(fourgo)
    elif strikes == 5:
        five = open('strikes/5.txt', 'r')
        fivego = five.read()
        print(fivego)
    elif strikes == 6:
        six = open('strikes/6.txt', 'r')
        sixgo = six.read()
        print(sixgo)
    else:
        print(" ")
    print(" ")
    print(" ")
    print(" ")
def show_result(strikes, limit, puzzle):
    if strikes < limit:
        print("You win!")
    else:
        print("You lose.")
        print("The word was " + puzzle + ".")



def play_again(name):
    while True:
        decision = input("Would you like to play again, " + name + "? (y/n) ")

        if decision.lower() == 'y' or decision.lower() == 'yes':
            print()
            return True
        elif decision.lower() == 'n' or decision.lower() == 'no':
            print()
            return False
        else:
            print("Please enter 'y' or 'n'.")
            
def play(file_names):

    for i,f in enumerate(file_names):
        print(str(i + 1) + ") " + f[:-4])
    choice = input("Which one?")
    choice = int(choice)

    file = "puzzles/" + file_names[choice - 1]
    
    puzzle = get_puzzle(file_names, file)
    guesses = ""
    solved = get_solved(puzzle, guesses)
    strikes = 0
    limit = 6

    print(solved)


    
    while solved != puzzle and strikes < limit:
        letter = get_guess(guesses)
        if letter not in puzzle:
            strikes += 1
            
      
        guesses += letter + ","
        solved = get_solved(puzzle, guesses)
        display_board(strikes, solved, guesses)
            

    show_result(strikes, limit, puzzle)
    
# Game is running here
name = input("Enter name: ")
show_start_screen()
instructions(name)
file_names = os.listdir("puzzles")

playing = True
while playing:
    play(file_names)
    playing = play_again(name)
end(name)
