# https://adventofcode.com/2023/day/2
import math

def part_1(lines):
    possible_games = []
    for line in lines:
        game, records = line.split(":")
        _, id = game.split()

        possible = True
        for subset in records.strip().split(";"):
            if not possible:
                break
            subset = subset.strip().split()

            for amount, color in zip(subset[::2], subset[1::2]):
                amount = int(amount)
                if "red" in color and amount > 12:
                    possible = False
                if "green" in color and amount > 13:
                    possible = False
                if "blue" in color and amount > 14:
                    possible = False

        if possible:
            possible_games.append(int(id))

    return sum(possible_games)

def part_2(lines):
    powers = []
    for line in lines:
        _, records = line.split(":")

        fewest_colors = {"red": 0, "green": 0, "blue": 0}
        for subset in records.strip().split(";"):
            subset = subset.strip().split()

            for amount, color in zip(subset[::2], subset[1::2]):
                amount = int(amount)
                for k, v in fewest_colors.items():
                    if k in color:
                        fewest_colors[k] = amount if not v else max(v, amount)

        powers.append(math.prod(fewest_colors.values()))

    return sum(powers)


with open("input") as f:
    lines = f.readlines()

    print("part 1:", part_1(lines))
    print("part 2:", part_2(lines))
