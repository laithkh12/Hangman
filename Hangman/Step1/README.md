# Step 1: Basic Setup

In this step, we set up the basic structure of the Word Guessing Game. The game randomly chooses a word from a predefined list and allows the user to guess a letter.

## Code Overview

- **Word List**: A list of words to choose from.
- **Random Word Selection**: Uses Python's `random` module to select a word.
- **User Input**: Prompts the user to guess a letter and checks if it is in the chosen word.

### Code Snippet

```python
import random

wordList = ["aardvark", "baboon", "camel"]
chosenWord = random.choice(wordList)
print(chosenWord)

guess = input("Guess a letter:\n").lower()
```
