import random
from collections import Counter


rules = {
    'rock': {
        'paper': -1,
        'rock': 0,
        'scissors': 1
    },
    'paper': {
        'paper': 0,
        'rock': 1,
        'scissors': -1
    },
    'scissors': {
        'paper': 1,
        'rock': -1,
        'scissors': 0
    }
}

winner = {-1: 'The computer wins.', 0: 'You tied.', 1: 'You win.'}

game_history = []
guess_options = ["rock", "paper", "scissors"]

while True:
    computer_guess = random.choice(guess_options)
    player_guess = "rock"  # input("Make your guess: ")

    if player_guess not in guess_options:
        print("Invalid guess, try again.")
        continue

    game_history.append(rules.get(player_guess).get(computer_guess))
    msg = f"[{len(game_history)}]: You chose <{player_guess}>, the computer chose <{computer_guess}>."

    print(f"{msg} {winner[game_history[-1]]}")

    c = Counter(game_history)

    if any((x > 1 for k, x in c.items() if k != 0)):
        winner = "You won."
        if c[-1] > 1:
            winner = f"The computer won."
        print(f"\n=======\nGame ends after {len(game_history)} rounds. ")
        print(f"There were {c[0]} ties, computer won {c[-1]} hands, you won {c[1]} hands.\n"
              f"{winner} ")
        break
