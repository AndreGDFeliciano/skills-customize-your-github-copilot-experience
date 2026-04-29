# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic word-guessing game using Python to practice string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Create the core game logic that selects a random word and tracks the player's guesses.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list using the `random` module
- Display the hidden word as underscores (e.g., `_ _ _ _ _`)
- Keep track of letters the player has already guessed


### 🛠️ Implement Game Loop and Win/Lose Conditions

#### Description
Add a game loop that accepts player input each turn and determines when the game ends.

#### Requirements
Completed program should:

- Accept a single letter guess from the player each turn
- Reveal correctly guessed letters in their positions
- Track and display the number of incorrect guesses remaining
- End the game when the word is fully guessed or attempts are exhausted
- Display an appropriate win or lose message at the end
