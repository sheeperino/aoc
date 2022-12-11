# https://adventofcode.com/2022/day/10

from typing import Iterable


def cycle_check(cycle: int, numbers: Iterable[int]) -> list[int] | list[None]:
    i = []
    if cycle in numbers:
        strength = cycle * addx
        i = [strength]
    return i


def print_screen(screen: str):
    for i, c in enumerate(screen, start=1):
        print(c, end="")
        if i % 40 == 0:  # new line every 40 chars
            print()


strengths = []

with open("input.txt") as f:
    addx = 1
    cycle = 1
    checkpoints = (20, 60, 100, 140, 180, 220)
    crt_screen = list("." * 240)

    for line in f:
        line = line.strip("\n")

        for _ in range(2):
            if (cycle % 40) - 1 in range(addx - 1, addx + 2):
                crt_screen[cycle - 1] = "#"
            else:
                crt_screen[cycle - 1] = "."
            strengths += cycle_check(cycle, checkpoints)
            cycle += 1
            # only 1 cycle if addx
            if "addx" not in line:
                break

        # add x in the end of these cycles
        if "addx" in line:
            n = int(line.split()[1])
            addx += n

print(sum(strengths))
print_screen(crt_screen)
