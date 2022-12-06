# https://adventofcode.com/2022/day/5


def main(part=None) -> str:
    top_of_each_stack = ""
    with open("input.txt") as f:
        crate_rows = []
        crate_stacks = {}
        # this is gonna be hell
        for line in f:
            line = line.strip("\n")
            if "[" in line:
                # replace empty item spots with a dot, remove spaces, remove brackets
                # dot is used temporarily to determine stack offset
                crate_row = line.replace("    ", ".")\
                                .replace(" ", "")\
                                .replace("[", "")\
                                .replace("]", "")
                crate_rows.append(crate_row)
            elif line.startswith(" 1"):
                # remove trailing whitespace
                number_line = line.split(" ")
                numbers = [int(n) for n in number_line if n.isdigit()]
                # create crate stacks
                for n in numbers:
                    _ = ""  # tmp var to join letters basically
                    for crate in crate_rows:
                        _ += crate[n-1]
                    crate_stacks[n] = _.replace(".", "")  # remove dot
                f.readline()  # skip blank line

            else:  # actual code starts here
                # parsing of lines is still not over lolll
                move, frm, to = [int(n) for n in line.split() if n.isdigit()]
                # debug -> print(f"move {move} from {crate_stacks[frm]} to {crate_stacks[to]}")
                stack_range = crate_stacks[frm][0:move]
                match part:
                    case 1:
                        # invert item sorting order (range) if multiple crates
                        crate_stacks[to] = stack_range[::-1] + crate_stacks[to]
                    case 2:
                        # dont invert if part 2
                        crate_stacks[to] = stack_range + crate_stacks[to]
                # remove range from starting stack
                crate_stacks[frm] = crate_stacks[frm].replace(
                    stack_range, "", 1)

        for i in crate_stacks.values():  # loop through keys
            if i:
                top_of_each_stack += i[0]  # get first char of string (top)
        return top_of_each_stack


print(main(part=1))
print(main(part=2))
