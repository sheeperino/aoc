# https://adventofcode.com/2023/day/4
from collections import defaultdict

def part_1(lines):
    points = []
    for line in lines:
        _, numbers = line.split(":")
        winning, own = numbers.split("|")
        winning = winning.strip().split()
        own = own.strip().split()

        common = set(own).intersection(set(winning))
        p = 2**(len(common)-1)
        points.append(int(p))

    return sum(points)


def part_2(lines):
    instances = defaultdict(int)
    for n, line in enumerate(lines, start=1):
        _, numbers = line.split(":")
        winning, own = numbers.split("|")
        winning = winning.strip().split()
        own = own.strip().split()

        common = set(own).intersection(set(winning))
        instances[n] += 1

        for j in range (n+1, len(common)+n+1):
            instances[j] += instances[n]

    return sum(instances.values())


with open("input") as f:
    lines = f.readlines()

    print("part 1:", part_1(lines))
    print("part 2:", part_2(lines))
