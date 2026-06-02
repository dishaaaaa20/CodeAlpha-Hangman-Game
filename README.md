# 🎮 Hangman Game

A simple text-based Hangman game built using Python. The player must guess a randomly selected word one letter at a time before running out of lives.

## 📌 Project Overview

This project is a console-based implementation of the classic Hangman game. A random word is chosen from a predefined list, and the player has 6 chances to guess incorrect letters. The game continues until the word is guessed completely or all lives are lost.

## 🚀 Features

- Random word selection
- Letter-by-letter guessing
- 6 incorrect attempts allowed
- Input validation
- Duplicate guess detection
- Win and lose conditions
- User-friendly console interface

## 🛠 Technologies Used

- Python 

## 📚 Concepts Used

- Variables
- Lists
- Strings
- Loops (`while`, `for`)
- Conditional Statements (`if`, `elif`, `else`)
- Functions (if implemented)
- User Input Handling
- Random Module

## 📂 Project Structure

```
Hangman-Game/
│
├── hangman.py
└── README.md
```

## ▶️ How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python hangman.py
```

## 🎯 Game Rules

1. A random word is selected from a predefined list.
2. The player guesses one letter at a time.
3. Correct guesses reveal the letter's position in the word.
4. Incorrect guesses reduce the remaining lives.
5. The player has a maximum of 6 incorrect attempts.
6. The game ends when:
   - The word is guessed successfully, or
   - All lives are exhausted.

## 💻 Sample Output

```text
========================================
        WELCOME TO HANGMAN
========================================

Word: _ _ _ _ _
Lives Remaining: 6

Guess a letter: a
Correct!

Word: a _ _ _ _
Lives Remaining: 6

Guess a letter: z
Wrong!

Lives Remaining: 5
```

## 🎓 Internship Task

This project was developed as part of a Python Programming Internship assignment to demonstrate understanding of basic programming concepts including loops, conditionals, lists, strings, and the random module.

## 📈 Future Improvements

- Multiple difficulty levels
- Categories of words
- Score tracking
- Hint system
- ASCII Hangman drawing
- Graphical User Interface (GUI)

## 👤 Author

Disha Jain
