import time

time_start = time.time()


def parse_input():

    file = open("input.txt")

    patterns = [
        [list(row) for row in pattern]
            for pattern in [
                case.split("\n") for case in file.read().split("\n\n")
            ]
        ]

    return patterns


def point_of_incidence():

    patterns = parse_input()

    total_sum = 0

    for pattern in patterns:

        i = j = 0

        width = len(pattern[0])
        height = len(pattern)


        for n in range(0, width - 1):
            for row in pattern:
                i = n
                j = i + 1

                while i >= 0 and j < width and row[i] == row[j]:
                    i -= 1
                    j += 1


                if i >= 0 and j < width:
                    break

            
            if i < 0 or j >= width:
                total_sum += (n + 1)
                break

    

        for n in range(0, height - 1):

            i = n
            j = i + 1

            while i >= 0 and j < height:
                if any(pattern[j][index] != column for index, column in enumerate(pattern[i])):
                    break

                i -= 1
                j += 1

            
            if i < 0 or j >= height:
                total_sum += 100 * (n + 1)
                break



    return total_sum


result = point_of_incidence()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")