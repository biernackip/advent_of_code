import collections
# input:
n_marbles = 70851*100
n_players = 477

# test values:
# n_marbles = 1618
# n_players = 10
# score = 8317

# n_marbles = 7999
# n_players = 13
# score = 146373

# n_marbles = 1104
# n_players = 17
# score = 2764

# n_marbles = 6111
# n_players = 21
# score = 54718

# n_marbles = 5807
# n_players = 30
# score = 37305


# n_marbles = 25
# n_players = 9

skip_marble = 23

player_scores = [0 for x in range(n_players)]
marble_array = []


def play_game(max_players, last_marble):
    scores = collections.defaultdict(int)
    circle = collections.deque([0])

    for marble in range(1, last_marble + 1):
        if marble % skip_marble == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0


print(play_game(n_players, n_marbles))
