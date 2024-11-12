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