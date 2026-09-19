import random

# List of 5 predefined words
words = ["python", "computer", "program", "developer", "keyboard"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_wrong_guesses = 6
wrong_guesses = 0

# Display hidden word
display_word = ["_"] * len(word)

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

while wrong_guesses < max_wrong_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether the letter is in the word
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Game result
if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over!")
    print("The word was:", word)
