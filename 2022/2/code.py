# https://adventofcode.com/2022/day/2

# part 1

# :P
strategy_guide = {
    "A": 1, "X": 1,  # rock
    "B": 2, "Y": 2,  # paper
    "C": 3, "Z": 3,  # scissors
    ("A", "Z"): 0, ("B", "X"): 0, ("C", "Y"): 0,  # loss
    ("A", "X"): 3, ("B", "Y"): 3, ("C", "Z"): 3,  # tie
    ("A", "Y"): 6, ("B", "Z"): 6, ("C", "X"): 6,  # win
}

your_total_score = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip("\n")
        opponent, you = line.split(" ")  # opponent and your shape
        your_points = strategy_guide[(opponent, you)] + strategy_guide[you]
        your_total_score += your_points

print(your_total_score)

# part 2

# :(
strategy_guide = {
    "X": 0,  # loss
    "Y": 3,  # tie
    "Z": 6,  # win
    ("A", "Y"): 1, ("B", "X"): 1, ("C", "Z"): 1,  # needs rock
    ("A", "Z"): 2, ("B", "Y"): 2, ("C", "X"): 2,  # needs paper
    ("A", "X"): 3, ("B", "Z"): 3, ("C", "Y"): 3,  # needs scissors
}

your_total_score = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip("\n")
        opponent, you = line.split(" ")
        your_points = strategy_guide[(opponent, you)] + strategy_guide[you]
        your_total_score += your_points

print(your_total_score)
# bad code, too lazy to rewrite
