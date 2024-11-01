
### Step 4: README.md

```markdown
# Step 4: Adding Lives and Losing Condition

In this step, we introduce a life tracking system. The user starts with a set number of lives and loses a life for each incorrect guess.

## Code Overview

- **Lives Variable**: Keeps track of the number of lives left for the user.
- **Losing Condition**: The game ends if the user runs out of lives.
- **ASCII Art**: Displays a hangman graphic corresponding to the number of lives left.
```
### Code Snippet

```python
lives = 6
stages = [...]  # Hangman stages ASCII art list

if guess not in chosenWord:
    lives -= 1
    if lives == 0:
        gameOver = True
        print("You Lose.")
        
print(stages[lives])
```
