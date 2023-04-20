## Did not work

import random


def player(prev_play, opponent_history=[]):
    # Create a transition matrix for the Markov chain
    transitions = {"R": {"R": 0, "P": 0, "S": 0}, "P": {"R": 0, "P": 0, "S": 0}, "S": {"R": 0, "P": 0, "S": 0}}

    # Update the transition matrix based on opponent's history
    if len(opponent_history) >= 2:
        for i in range(len(opponent_history) - 1):
            prev = opponent_history[i]
            curr = opponent_history[i + 1]
            transitions[prev][curr] += 1

    # Check if prev_play is a valid value ("R", "P", or "S")
    if prev_play not in ["R", "P", "S"]:
        prev_play = random.choice(["R", "P", "S"])  # Choose a random play as fallback

    # Calculate the probabilities for the next play
    total_count = sum(transitions[prev_play].values())
    if total_count == 0:
        # If total_count is zero, choose a random play as fallback
        choices = ["R", "P", "S"]
        next_play = random.choice(choices)
    else:
        probabilities = {move: count / total_count for move, count in transitions[prev_play].items()}
        # Choose the next play based on the calculated probabilities
        choices = ["R", "P", "S"]
        next_play = random.choices(choices, weights=list(probabilities.values()))[0]

    return next_play
