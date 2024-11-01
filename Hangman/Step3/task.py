import random

wordList = ["aardvark", "baboon", "camel"]

chosenWord = random.choice(wordList)
print(chosenWord)

placeholder = ""
for position in range(len(chosenWord)):
    placeholder += "_"
print(placeholder)

# TODO 1 : Use a while loop to let the user guess again
gameOver = False
correctLetters = []

while not gameOver:
    guess = input("Guess a letter:\n").lower()
    display = ""
    # TODO 2 : Change the for loop so that you keep the previous correct

    for letter in chosenWord:
        if letter == guess:
            display += letter
            correctLetters.append(guess)
        elif letter in correctLetters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        gameOver = True
        print("You Win.")



