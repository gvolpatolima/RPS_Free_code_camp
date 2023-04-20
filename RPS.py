#
# # 60% winrate on Kris
#
# import random
#
# def player(prev_play, opponent_history=[], play_order=[{
#     "RR": 0,
#     "RP": 0,
#     "RS": 0,
#     "PR": 0,
#     "PP": 0,
#     "PS": 0,
#     "SR": 0,
#     "SP": 0,
#     "SS": 0,
# }]):
#
#     if not prev_play:
#         prev_play = random.choice(["R", "P", "S"])
#     opponent_history.append(prev_play)
#
#     last_two = "".join(opponent_history[-2:])
#     if len(last_two) == 2:
#         play_order[0][last_two] += 1
#
#     potential_plays = [
#         prev_play + "R",
#         prev_play + "P",
#         prev_play + "S",
#     ]
#
#     sub_order = {
#         k: play_order[0][k]
#         for k in potential_plays if k in play_order[0]
#     }
#
#     prediction = max(sub_order, key=sub_order.get)[-1:]
#
#     # To win against the abbey bot, we can use the same move as its predicted move
#     return prediction
#
# # 100% winrate on quinncy
#
# def player(prev_play, opponent_history=[]):
#     # Define the moves and their corresponding winning moves
#     moves = {"R": "P", "P": "S", "S": "R"}
#
#     # If previous play is available, determine the winning move
#     if prev_play:
#         winning_move = moves[prev_play]
#         return winning_move
#     else:
#         # If previous play is not available, make a random move
#         import random
#         return random.choice(["R", "P", "S"])
#
#
# 76% winrate on mrugesh
# import random
# def player(prev_play, opponent_history=[], play_order=[{
#     "RR": 0,
#     "RP": 0,
#     "RS": 0,
#     "PR": 0,
#     "PP": 0,
#     "PS": 0,
#     "SR": 0,
#     "SP": 0,
#     "SS": 0,
# }], counter=[0]):
#
#     if not prev_play:
#         prev_play = random.choice(["R", "P", "S"])
#     opponent_history.append(prev_play)
#
#     last_two = "".join(opponent_history[-2:])
#     if len(last_two) == 2:
#         play_order[0][last_two] += 1
#
#     potential_plays = [
#         prev_play + "R",
#         prev_play + "P",
#         prev_play + "S",
#     ]
#
#     sub_order = {
#         k: play_order[0][k]
#         for k in potential_plays if k in play_order[0]
#     }
#
#     prediction = max(sub_order, key=sub_order.get)[-1:]
#
#     # Add strategic moves based on observed patterns
#     if counter[0] > 10:
#         if "R" in opponent_history[-3:]:
#             prediction = "P"
#         elif "P" in opponent_history[-3:]:
#             prediction = "S"
#         elif "S" in opponent_history[-3:]:
#             prediction = "R"
#
#     counter[0] += 1
#
#     # To win against the abbey bot, we can use the same move as its predicted move
#     return prediction
#

import random
def player(prev_play, opponent_history=[]):
    if len(opponent_history) == 0:
        # first move: play random
        next_move = random.choice(['R', 'P', 'S'])
    else:
        last_opponent_move = opponent_history[-1]

        if len(opponent_history) <= 1000:
            # play the last move the first bot played
            next_move = last_opponent_move
        elif len(opponent_history) <= 2000:
            # play P for all 1000 iterations against the second bot
            next_move = 'P'
        elif len(opponent_history) <= 3000:
            # play the move that counters the opponent's last move for 1000 iterations against the third bot
            if last_opponent_move == 'R':
                next_move = 'P'
            elif last_opponent_move == 'P':
                next_move = 'S'
            else:
                next_move = 'R'
        else:
            # play S for all 1000 iterations against the last bot
            next_move = 'S'

    return next_move
    return next_move