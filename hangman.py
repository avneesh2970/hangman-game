import random

def choose_word():
    words = ["python", "hangman", "programming", "challenge", "developer", "gaming"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    while True:
        word_to_guess = choose_word()
        guessed_letters = []
        attempts = 5

        print("\nWelcome to Hangman!")
        print("The word starts with: " + word_to_guess[0])
        print("The word ends with: " + word_to_guess[-1])

        while attempts > 0:
            print("\nAttempts left:", attempts)
            current_display = display_word(word_to_guess, guessed_letters)
            print("Current word:", current_display)

            guess = input("Enter a letter: ").lower()

            if guess.isalpha() and len(guess) == 1:
                if guess in guessed_letters:
                    print("You already guessed that letter. Try again.")
                elif guess in word_to_guess:
                    print("Good guess!")
                else:
                    print("Incorrect guess.")
                    attempts -= 1

                guessed_letters.append(guess)

                if set(word_to_guess) == set(guessed_letters):
                    print("\nCongratulations! You guessed the word:", word_to_guess)
                    
                    break
            else:
                print("Invalid input. Please enter a single letter.")

        if attempts == 0:
            print("\nSorry, you ran out of attempts. The word was:", word_to_guess)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    hangman()
