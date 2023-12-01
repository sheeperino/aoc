# https://adventofcode.com/2023/day/1

with open("input") as f:
    calibration_values = []
    for line in f:
        digits_only = list(filter(lambda x: x.isdigit(), line))
        calibration = int(digits_only[0] + digits_only[-1])
        calibration_values.append(calibration)

    answer_1 = sum(calibration_values)
    print(answer_1)

