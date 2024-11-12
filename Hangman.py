print("Welcome to hangman game\n")

def get_word():
    word = input("Please provide a word to guess: ")
    return word.upper()

def display_current_progress(word, guessed_letters):
    """Function to display the current progress of the guessed word."""
    display = ""
    for letter in word:
        if letter in guessed_letters or letter == " ":
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def play_hangman():
    # Initialization
    word = get_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6
    hangman_pics = [
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
    ]

    print("Welcome to Hangman!")
    print(hangman_pics[0])

    # Game loop
    while incorrect_guesses < max_incorrect:
        print("\n" + display_current_progress(word, guessed_letters))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))  # Display guessed letters
        guess = input("Guess a letter: ").upper()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word if letter != " "):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            incorrect_guesses += 1
            guessed_letters.add(guess)
            print(f"Sorry, '{guess}' is not in the word.")
            print(hangman_pics[incorrect_guesses])

        if incorrect_guesses == max_incorrect:
            print("\nGame Over! The word was:", word)

play_hangman()