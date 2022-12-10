# https://adventofcode.com/2022/day/9

MOVEMENTS = {
    "R": (0, +1),
    "L": (0, -1),
    "U": (+1, 0),
    "D": (-1, 0)
}

with open("input.txt") as f:
    lines = [line.strip("\n") for line in f]
    width = 0
    height = 0
    r = l = u = d = 0
    for line in lines:
        direction, amount = line.split()
        amount = int(amount)
        match direction:
            case "R":
                if amount > r:
                    r = amount
            case "L":
                if amount > l:
                    l = amount
            case "U":
                if amount > u:
                    u = amount
            case "D":
                if amount > d:
                    d = amount

        width = abs(r * l) * 2 + 1
        height = abs(u * d) * 2 + 1
        x, y = abs(r - l), abs(u - d)

    # create a width * 2 + 2 * height + 1 grid
    grid = [[0 for i in range(width)] for j in range(height)]

    # starting point (x, y) for head and tail
    H = [x, y]
    T = [x, y]
    grid[T[0]][T[1]] = 1  # starting position counts as visited

    buffer = []  # buffer of moves

    for line in lines:
        direction, amount = line.split()
        amount = int(amount)

        for _ in range(amount):
            # move H in <direction> by <amount> times
            H = H[0] + MOVEMENTS[direction][0], H[1] + MOVEMENTS[direction][1]
            # check if H is in a 3x3 area surrounding T
            adjacent = any(H[0] == j and H[1] == i
                           for j in range(T[0] - 1, T[0] + 2)  # (2nd argument is exclusive)
                           for i in range(T[1] - 1, T[1] + 2)
                           )
            if not adjacent:
                # do all moves in buffer
                # better alternative to using math for diagonals
                # also fixes eventual edge cases
                for move in buffer:
                    T = T[0] + MOVEMENTS[move][0], T[1] + MOVEMENTS[move][1]
                grid[T[0]][T[1]] = 1
                # clear after executing moves
                buffer.clear()

            # add to buffer after every H move
            buffer.append(direction)

tiles_visited = sum(map(sum, grid))
print(tiles_visited)
