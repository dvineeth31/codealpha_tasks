import random

# Predefined list of words
words = ["apple", "table", "snake", "radio", "watch"]

word = random.choice(words)
guessed = ["_"] * len(word)
incorrect_guesses = 0
max_guesses = 6
guessed_letters = []

while incorrect_guesses < max_guesses and "_" in guessed:
    print("Word:", " ".join(guessed))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)

    if guess in word:
        for idx, letter in enumerate(word):
            if letter == guess:
                guessed[idx] = guess
    else:
        incorrect_guesses += 1
        print(f"Incorrect guess! ({incorrect_guesses} out of {max_guesses})")

if "_" not in guessed:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)
