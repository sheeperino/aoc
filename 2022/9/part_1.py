# https://adventofcode.com/2022/day/9

MOVEMENTS = {
    "R": (0, +1),
    "L": (0, -1),
    "U": (+1, 0),
    "D": (-1, 0)
}


def is_adjacent(H: tuple | list, T: tuple | list) -> bool:
    # check if H is in a 3x3 area surrounding T
    for i in range(T[0] - 1, T[0] + 2):
        for j in range(T[1] - 1, T[1] + 2):
            if H[0] == i and H[1] == j:
                return True
    return False


with open("input_test.txt") as f:
    lines = [line.strip("\n") for line in f]
    # starting point (x, y) for head and tail
    H = (0, 0)
    T = (0, 0)
    visited = set()
    visited.add((0, 0))
    buffer = []  # buffer of moves

for line in lines:
    direction, amount = line.split()
    amount = int(amount)

    for _ in range(amount):
        # move H in <direction> by <amount> times
        H = H[0] + MOVEMENTS[direction][0], H[1] + MOVEMENTS[direction][1]

        if not is_adjacent(H, T):
            # do all moves in buffer
            # better alternative to using math for diagonals
            # also fixes eventual edge cases
            for move in buffer:
                T = T[0] + MOVEMENTS[move][0], T[1] + MOVEMENTS[move][1]
            visited.add((T[0], T[1]))
            # clear after executing moves
            buffer.clear()

        # add to buffer after every H move
        buffer.append(direction)

visited = len(visited)
print(visited)
