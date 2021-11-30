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
hand_history = []  # store -1, 0 or 1 each hand
guess_options = ["rock", "paper", "scissors"]

while True:
    computer_guess = random.choice(guess_options)
    player_guess = input("Make a guess: ").lower()

    if player_guess not in guess_options:
        print("Invalid data entry, try again.")
        continue

    hand_history.append(rules.get(player_guess).get(computer_guess))
    msg = f"[{len(hand_history)}]: You chose <{player_guess}>, the computer chose <{computer_guess}>."
    print(f"{msg} {winner[hand_history[-1]]}")

    c = Counter(hand_history)

    if any((x > 1 for k, x in c.items() if k != 0)):

        winner = "You won."
        if c[-1] > 1:
            winner = f"The computer won."
        print(f"\n=======\nGame ends after {len(hand_history)} rounds. ")
        print(f"There were {c[0]} ties, computer won {c[-1]} hands, you won {c[1]} hands.\n"
              f"{winner} ")

        break
