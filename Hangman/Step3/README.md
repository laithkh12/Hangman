# Step 3: Implementing a Loop for Guesses

In this step, we implement a loop that allows the user to keep guessing letters until they either guess the word correctly or run out of lives.

## Code Overview

- **While Loop**: This loop continues to ask for user input until the game is over.
- **Correct Letters Tracking**: Maintains a list of correctly guessed letters to ensure they are displayed properly.

### Code Snippet

```python
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

    if "_" not in display:
        gameOver = True
        print("You Win.")
```
