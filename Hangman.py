# print("Welcome to hangman game\nProvide player names.")
# player1 = input("Player 1: ")
# print(f"Player 1 is {player1}\n")
# player2 = input("Player 2: ")
# print(f"Player 2 is {player2}\n")
# print("Player one provides a word to guess")
# word = input("Please provide a word to guess: ")
# print(f"Word to guess: {len(word)*'_'}")

def get_word():
    word = input("Please provide a word to guess: ")
    return word.upper()

def display_current_progress(word, guessed_letters):
    """Function to display the current progress of the guessed word."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
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