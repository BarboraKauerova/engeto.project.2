'''
      author = Barbora Kauerova
      discord = barborakauerova_12439
      email = kauerova.barbora.bk@gmail.com
'''

import random

def make_secret_code():
    """Creates a secret code with 4 different numbers."""
    all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(all_numbers)
    secret_code = all_numbers[:4]
    return secret_code

def get_player_guess():
    """Asks the player for their guess and checks if it's valid."""
    while True:
        guess = input(">>> ")  # Výzva byla změněna tak, aby odpovídala požadovanému výstupu
        if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
            return [int(digit) for digit in guess]
        else:
            print("Oops! Please enter 4 different numbers.")

def check_guess(secret_code, player_guess):
    """Checks how many bulls and cows the player got."""
    bulls = 0
    cows = 0

    for i in range(4):
        if secret_code[i] == player_guess[i]:
            bulls += 1
        elif player_guess[i] in secret_code:
            cows += 1

    return bulls, cows

def evaluate_performance(tries):
    """Evaluates the player's performance based on the number of tries."""
    if tries <= 4:
        return "amazing!"
    elif tries <= 8:
        return "average."
    else:
        return "not so good..."

def play_game():
    """The main part of the game."""
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    print("Enter a number:")
    print("-----------------------------------------------") 

    secret_code = make_secret_code()
    tries = 0

    while True:
        player_guess = get_player_guess()
        tries += 1

        bulls, cows = check_guess(secret_code, player_guess)
        print(f"{bulls} bulls, {cows} cows")
        print("-----------------------------------------------")

        if bulls == 4:
            print(f"Correct, you've guessed the right number in {tries} guesses!")
            print("-----------------------------------------------")
            print(f"That's {evaluate_performance(tries)}")
            break

if __name__ == "__main__":
    play_game()
