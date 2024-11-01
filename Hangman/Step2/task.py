import random

wordList = ["aardvark", "baboon", "camel"]

chosenWord = random.choice(wordList)
print(chosenWord)

# TODO 1 : Create a "placeholder" with the same number of blanks
placeholder = ""
for position in range(len(chosenWord)):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter:\n").lower()

# TODO 2 : Create a "display" that puts the guess letter in the right position
display = ""



for letter in chosenWord:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)