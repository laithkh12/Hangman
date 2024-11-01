
#### Step 2: README.md

```markdown
# Step 2: Adding Placeholders

In this step, we create a placeholder for the chosen word, which will be displayed as underscores for each letter in the word.

## Code Overview

- **Placeholder Creation**: Generates a string of underscores corresponding to the length of the chosen word.
- **User Input**: Continues to allow the user to guess letters.

### Code Snippet

```python
placeholder = ""
for position in range(len(chosenWord)):
    placeholder += "_"
print(placeholder)
```
