# https://adventofcode.com/2022/day/4

def section_to_set(section: str) -> set[int]:
    """convert section to range then to set"""
    # split sections in start and finish
    start, end = section.split("-")
    # make section an inclusive range
    section_range = range(int(start), int(end)+1)
    return set(section_range)


with open("input.txt") as f:
    superset_ranges = 0
    overlapping_ranges = 0

    for line in f:
        pair = line.strip("\n")
        s1, s2 = pair.split(",")  # sections 1 and 2
        s1, s2 = section_to_set(s1), section_to_set(s2)

        # check if s1 and s2 overlap (not disjoint)
        if not s1.isdisjoint(s2):
            overlapping_ranges += 1
            # check if section1 fully contains section2 and viceversa
            if s1.issuperset(s2) or s2.issuperset(s1):
                superset_ranges += 1

print(superset_ranges)
print(overlapping_ranges)
