# https://adventofcode.com/2023/day/1

def part_1(lines):
    calibration_values = []
    for line in lines:
        digits_only = list(filter(lambda x: x.isdigit(), line))
        calibration = int(digits_only[0] + digits_only[-1])
        calibration_values.append(calibration)

    return sum(calibration_values)

def part_2(lines):
    calibration_values = []
    allowed_digits = {
        "one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r",
        "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"
    }

    for line in lines:
        for k, v in allowed_digits.items():
            line = line.replace(k, v)

        digits_only = list(filter(lambda x: x.isdigit(), line))
        calibration = int(digits_only[0] + digits_only[-1])
        calibration_values.append(calibration)

    return sum(calibration_values)


with open("input") as f:
    lines = f.readlines()

    print("part 1:", part_1(lines))
    print("part 2:", part_2(lines))
