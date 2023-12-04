fdin = open("input.txt")

def trebuchet(fdin):

    total_sum = 0

    for line in fdin:
        first_number = 0
        second_number = 0

        for char in line:
            if char.isdigit():
                first_number = int(char)
                break

        for i in range(len(line)-1, -1, -1):
            if line[i].isdigit():
                second_number = int(line[i])
                break

        final_number = (first_number * 10) + second_number
        total_sum += final_number

    return total_sum


print(trebuchet(fdin))