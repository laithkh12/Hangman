import random
stages = ['''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========
''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
========
''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
========
''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
========
''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
========
''', '''
 +---+
 |   |
 O   |
     |
     |
     |
========
''', '''
 +---+
 |   |
     |
     |
     |
     |
========
''']

wordList = ["aardvark", "baboon", "camel"]

# TODO 1 : Create a variable called 'lives' to keep track of the lives. Set 'lives' to equal 6
lives = 6

chosenWord = random.choice(wordList)
print(chosenWord)

placeholder = ""
for position in range(len(chosenWord)):
    placeholder += "_"
print(placeholder)

gameOver = False
correctLetters = []

while not gameOver:
    guess = input("Guess a letter:\n").lower()
    display = ""
    for letter in chosenWord:
        if letter == guess:
            display += letter
            correctLetters.append(guess)
        elif letter in correctLetters:
            display += letter
        else:
            display += "_"
    print(display)

    # TODO 2 : If guess is not a letter in the chosenWord,then reduce 'lives' by 1. If lives goes down to 0 then the game should stop and it should print "You Lose."
    if guess not in chosenWord:
        lives -= 1
        if lives == 0:
            gameOver = True
            print("You Lose.")

    if "_" not in display:
        gameOver = True
        print("You Win.")

    # TODO 3 : Print the ASCII art from 'stages', that corresponds to the current number of 'lives' the user has remaining
    print(stages[lives])

