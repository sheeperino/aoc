# https://adventofcode.com/2023/day/3
from string import punctuation as symbols
symbols = symbols.replace(".", "")

def part_1(lines):
    part_numbers = []

    number = ""  # any number
    adjacent = False
    for y, row in enumerate(lines):
        for x, t in enumerate(row.strip()):
            if t.isdigit():
                # check if a digit is adjacent to a symbol
                for dx, dy in [(0, 1), (1, 1), (1, 0),
                               (0, -1), (-1, 0), (-1, -1),
                               (-1, 1), (1, -1)]:
                    if adjacent:
                        break
                    try:
                        adjacent = lines[y+dy][x+dx] in symbols
                    except IndexError:
                        pass

                number += t
            else:
                if number and adjacent:
                    part_numbers.append(int(number))
                    adjacent = False
                number = ""

    return sum(part_numbers)


def part_2(lines):
    gear_ratios = []
    star_symbol_coords = {}

    number = ""  # any number
    symbol_coords = ()
    adjacent = False
    for y, row in enumerate(lines):
        for x, t in enumerate(row.strip()):
            if t.isdigit():
                # check adjacency
                for dx, dy in [(0, 1), (1, 1), (1, 0),
                               (0, -1), (-1, 0), (-1, -1),
                               (-1, 1), (1, -1)]:
                    if adjacent:
                        break
                    try:
                        adjacent = lines[y+dy][x+dx] == "*"
                        if adjacent:
                            symbol_coords = (x+dx, y+dy)
                    except IndexError:
                        pass

                number += t
            else:
                if number and adjacent:
                    number = int(number)
                    adjacent = False
                    if symbol_coords not in star_symbol_coords:
                        star_symbol_coords[symbol_coords] = number
                    else:
                        gear_ratios.append(star_symbol_coords[symbol_coords] * number)
                        # all the next operations will be 0
                        star_symbol_coords[symbol_coords] = 0
                    symbol_coords = ()
                number = ""

    return sum(gear_ratios)


with open("input") as f:
    lines = f.readlines()

    print("part 1:", part_1(lines))
    print("part 2:", part_2(lines))
