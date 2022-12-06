# https://adventofcode.com/2022/day/6

with open("input.txt") as f:
    for line in f:
        line = line.strip("\n")
    
        # part 1
        processed_chars = 0
        start, end = 0, 4  # start and end of 4-characters chunk
        while True:
            chunk = line[start:end]  # check chunk of 4 characters each time
            if len(chunk) == len(set(chunk)):  # check if chunk has duplicates using len
                # finally add length of chunk to the processed_chars
                processed_chars += len(chunk)
                break
            # increase chunk position and processed_chars
            # at the end of each iteration
            start += 1
            end += 1
            processed_chars += 1

        print(processed_chars)

        # part 2
        processed_chars = 0
        start, end = 0, 14  # start and end of 14-characters chunk
        while True:
            chunk = line[start:end]  # check chunk of 14 characters each time
            if len(chunk) == len(set(chunk)):  # check if chunk has duplicates using len
                # finally add length of chunk to the processed_chars
                processed_chars += len(chunk)
                break
            # increase chunk position and processed_chars
            # at the end of each iteration
            start += 1
            end += 1
            processed_chars += 1

        print(processed_chars)
