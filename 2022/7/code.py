# https://adventofcode.com/2022/day/7

from collections import defaultdict

with open("input.txt") as f:
    MAX_SIZE = 100000
    path = []
    dir_sizes_unique = defaultdict(int)
    for line in f:
        line = line.strip("\n")

        commands = line.split()
        if (commands[0], commands[1]) == ("$", "cd"):
            if commands[2] == "..":
                path = path[:-1]
                cwd = path[-1]
            else:
                cwd = commands[2]
                path.append(cwd)
        elif commands[0].isdigit():
            file_size = int(commands[0])
            # add size to parent directories and itself
            for n, _ in enumerate(path, start=1):
                dir = ".".join(path[:n])
                dir_sizes_unique[dir] += file_size

    total_size_all = sum([
        size for size in dir_sizes_unique.values() if size <= MAX_SIZE
    ])

    MAX_SPACE = 70000000
    SPACE_FOR_UPDATE = 30000000
    unused_space = MAX_SPACE - sorted(dir_sizes_unique.values())[-1]
    smallest_dir = min([  # smallest dir to delete for update
        size
        for size in sorted(dir_sizes_unique.values(), reverse=True)
        if size >= (SPACE_FOR_UPDATE - unused_space)
    ])

print(total_size_all)
print(smallest_dir)
