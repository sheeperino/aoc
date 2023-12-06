# https://adventofcode.com/2023/day/6

def part_1(lines):
    times = []
    distances = []
    margin = 1

    # parse
    times = map(int, lines[0].replace("Time:","").split())
    distances = map(int, lines[1].replace("Distance:","").split())

    for t, min_d in zip(times, distances):
        # the race
        times_beaten = 0
        for s in range(1, t):
            r = t - s
            d = r * s
            if d > min_d:
                times_beaten += 1
        margin *= times_beaten

    return margin


def part_2(lines):
    times_beaten = 0

    time = lines[0].replace("Time:","").split()
    time = int("".join(time))

    min_d = lines[1].replace("Distance:","").split()
    min_d = int("".join(min_d))

    # the race
    for s in range(1, time):
        r = time - s
        d = r * s
        if d > min_d:
            times_beaten += 1

    return times_beaten


with open("input") as f:
    lines = f.readlines()

    print("part 1:", part_1(lines))
    print("part 2:", part_2(lines))
