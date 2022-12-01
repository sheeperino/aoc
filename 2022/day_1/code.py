# https://adventofcode.com/2022/day/1

highest_calories = []

with open("input.txt") as f:
    elf_calories = 0  # calories that each elf has
    for line in f:
        line = line.strip("\n")  # remove "\n" found at the end of lines
        if line == "":
            highest_calories.append(elf_calories)
            elf_calories = 0
            continue  # avoid adding the empty line
        elf_calories += int(line)
    else:
        # add last line manually
        highest_calories.append(elf_calories)

    # sort calories from highest to lowest
    highest_calories.sort(reverse=True)

print(highest_calories[0])
print(sum(highest_calories[0:3]))
