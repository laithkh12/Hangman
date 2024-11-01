
import  random

# TODO 1 : Update the word list to use the wordList from hangman_words.py
import hangman_words
import hangman_art

lives= 6

# TODO 3 : Import the logo from hangman_art.py
print(hangman_art.logo)

chosenWord = random.choice(hangman_words.wordList)
print(chosenWord)

placeholder = ""
wordLength = len(chosenWord)
for position in range(wordLength):
    placeholder += "_"
print("Word to guess: " + placeholder)

gameOver = False
correctLetters = []
while not gameOver:
    # TODO 6 : Update the code below to tell the user how many lives they have left
    print(f"******************************{lives}/6 LIVES LEFT **********************************")
    guess = input("Guess a letter: ").lower()

    # TODO 4 : If the user has entered a letter they've already guessed, print the letter
    if guess in correctLetters:
        print(f"You've already guessed {guess}")

    display = ""
    for letter in chosenWord:
        if letter == guess:
            display += letter
            correctLetters.append(guess)
        elif letter in correctLetters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosenWord:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        if lives == 0:
            gameOver = True

            print(f"******************************IT WAS {chosenWord}! YOU LOSE **********************************")

    if "_" not in display:
        gameOver = True
        print("****************************** YOU WIN **********************************")

    print(hangman_art.stages[lives])




