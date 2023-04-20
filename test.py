import random


def generate_markov_chain(corpus, n=1):
    markov_chain = {}

    # Loop through the corpus to generate the Markov chain
    for i in range(len(corpus)):
        if i + n < len(corpus):
            prefix = tuple(corpus[i:i + n])  # Use a tuple as the key for the prefix
            suffix = corpus[i + n]  # Use the next word as the suffix

            if prefix in markov_chain:
                markov_chain[prefix].append(suffix)
            else:
                markov_chain[prefix] = [suffix]

    return markov_chain


def get_opponent_play(prev_play, opponent_history):
    opponent_history.append(prev_play)  # Add the previous play to the history
    prefix = tuple(opponent_history[-n:])  # Use the last n plays as the prefix

    if prefix in markov_chain:
        suffixes = markov_chain[prefix]
        return random.choice(suffixes)
    else:
        return random.choice(["rock", "paper", "scissors"])  # If prefix not found, choose randomly


# Global variables
corpus = ["rock", "paper", "scissors"]  # Corpus of possible plays
n = 2  # Set the order of the Markov chain (prefix length)
markov_chain = generate_markov_chain(corpus, n)  # Generate the Markov chain


def player(prev_play, opponent_history=[]):
    opponent_play = get_opponent_play(prev_play, opponent_history)
    return opponent_play


# Example usage
prev_play = "rock"
opponent_history = ["scissors", "paper", "rock"]
next_play = player(prev_play, opponent_history)
print("Next play:", next_play)
