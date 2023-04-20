import random

def player(p1_prev_play, opponent_history=[], n=2, corpus=["rock", "paper", "scissors"], markov_chain={}):
    # Check if p1_prev_play is in opponent_history
    if p1_prev_play in opponent_history:
        sub_order = {}
        for i in range(len(opponent_history)):
            if opponent_history[i] == p1_prev_play and i + n < len(opponent_history):
                suffix = opponent_history[i + n]
                if suffix in sub_order:
                    sub_order[suffix] += 1
                else:
                    sub_order[suffix] = 1

        # Check if sub_order is not empty
        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]
        else:
            prediction = random.choice(corpus)  # Choose randomly if sub_order is empty
    else:
        prediction = random.choice(corpus)  # Choose randomly if p1_prev_play is not in opponent_history

    return prediction
