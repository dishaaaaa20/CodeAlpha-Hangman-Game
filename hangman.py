import random

words = ["Internship", "Coding", "Computer", "Technology", "Hardware"]

word = random.choice(words)
guessed_letters = []
lives = 6

print("=" * 40)
print("        WELCOME TO HANGMAN")
print("=" * 40)

while lives > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Lives Remaining:", lives)

    if "_" not in display:
        print("\n🎉 You Won!")
        print("The word was:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        lives -= 1
        print("❌ Wrong!")

if lives == 0:
    print("\n💀 Game Over!")
    print("The word was:", word)
