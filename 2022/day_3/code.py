# https://adventofcode.com/2022/day/3/input

import string

# generate `letter: number` table
priorities = dict(zip(
    string.ascii_letters,
    range(1, 53)
))


# part 1

total_priority = 0

with open("input.txt") as f:
    for line in f:
        rucksack = line.strip("\n")

        # split rucksack in half to get both compartments
        comp1, comp2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        # convert to set (remove duplicates too c:)
        comp1, comp2 = set(comp1), set(comp2)
        # find item in common with set intersection then convert to str
        item_in_common = "".join(comp1.intersection(comp2))
        item_priority = priorities[item_in_common]  # get item priority

        total_priority += item_priority

print(total_priority)

# part 2
# kinda messy :/

total_priority = 0

with open("input.txt") as f:
    prev_rucksack = set()

    for i, line in enumerate(f, start=1):
        rucksack = set(line.strip("\n"))
        # exhaustive set intersection
        if len(prev_rucksack) == 0:
            prev_rucksack = rucksack
        prev_rucksack = set.intersection(rucksack, prev_rucksack)

        # get item in common every 3 iterations (1 group of rucksacks)
        if i % 3 == 0:
            item_in_common = "".join(prev_rucksack)
            item_priority = priorities[item_in_common]  # get item priority
            total_priority += item_priority
            prev_rucksack.clear()  # empty set

print(total_priority)
