# https://adventofcode.com/2022/day/8

visible_trees = 0
highest_scenic_score = 0

with open("input.txt") as f:
    rows = [line.strip() for line in f.readlines()]

# add edges to visible trees
visible_trees += len(rows[0]) + len(rows[-1]) + 2 * (len(rows)-2)

for i, row in enumerate(rows):
    # skip first and last row
    if i == 0 or i == len(rows) - 1:
        continue

    for j, tree in enumerate(row):
        # skip first and last tree
        if j == 0 or j == len(row) - 1:
            continue

        right = all(tree > tile for tile in row[j + 1:])
        left = all(tree > tile for tile in row[:j])
        down = all(tree > tile[j] for tile in rows[i + 1:])
        up = all(tree > tile[j] for tile in rows[:i])

        if right or left or down or up:
            visible_trees += 1

        right = 0
        for tile in row[j + 1:]:
            right += 1
            if tree <= tile:
                break

        left = 0
        for tile in row[j - 1::-1]:
            left += 1
            if tree <= tile:
                break

        down = 0
        for tile in rows[i + 1:]:
            down += 1
            if tree <= tile[j]:
                break

        up = 0
        for tile in rows[i - 1::-1]:
            up += 1
            if tree <= tile[j]:
                break

        scenic_score = right * left * down * up
        if scenic_score > highest_scenic_score:
            highest_scenic_score = scenic_score

print(visible_trees)
print(highest_scenic_score)
