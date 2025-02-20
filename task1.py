import random

def choose_word():
    words = ["python", "hangman", "computer", "programming", "developer", "software"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def get_guess():
    # Simulating user input for non-interactive environments
    simulated_inputs = ["p", "y", "t", "h", "o", "n"]
    if get_guess.counter < len(simulated_inputs):
        guess = simulated_inputs[get_guess.counter]
        get_guess.counter += 1
        print(f"Simulated input: {guess}")
        return guess
    return ""
get_guess.counter = 0

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Maximum incorrect guesses allowed
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = get_guess().lower()
        
        if not guess:
            print("No more simulated inputs. Exiting...")
            break
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame Over! The word was:", word)

if __name__ == "__main__":
    hangman()

