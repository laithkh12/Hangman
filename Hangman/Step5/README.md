
### Step 5: README.md

```markdown
# Step 5: Modularizing Code with Separate Files

In this final step, we refactor the code to make it more organized by placing the word list and ASCII art in separate files.

## Code Overview

- **Modularization**: The word list is moved to `hangman_words.py`, and the ASCII art is moved to `hangman_art.py`.
- **Importing Modules**: The main game file now imports the necessary modules to access the word list and art.
```
### Code Snippet

```python
import hangman_words
import hangman_art

chosenWord = random.choice(hangman_words.wordList)
print(hangman_art.logo)
```
