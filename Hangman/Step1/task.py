wordList = ["aardvark", "baboon", "camel"]

# TODO 1 : Randomly choose a word from the list and assign it to a variable called chosenWord. Then print it
import random
chosenWord = random.choice(wordList)
print(chosenWord)

# TODO 2 : Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
guess = input("Guess a letter:\n").lower()
print(guess)

# TODO 3 : Check if the letter the user guessed is one of the letters in the chosenWord. Print "Right" if it is, "Wrong" if it's not.
for letter in chosenWord:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")