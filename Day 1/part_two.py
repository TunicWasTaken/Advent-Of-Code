import re

fdin = open("input.txt")

def transform(num):

    num = num.group(0)
    match num:
        case "one":
            return '1'
        case "two":
            return '2'
        case "three":
            return '3'
        case "four":
            return '4'
        case "five":
            return '5'
        case "six":
            return '6'
        case "seven":
            return '7'
        case "eight":
            return '8'
        case "nine":
            return '9'
        
def transformrev(num):

    num = num.group(0)
    match num:
        case "eno":
            return '1'
        case "owt":
            return '2'
        case "eerht":
            return '3'
        case "ruof":
            return '4'
        case "evif":
            return '5'
        case "xis":
            return '6'
        case "neves":
            return '7'
        case "thgie":
            return '8'
        case "enin":
            return '9'
        

def trebuchet(fdin):
    total_sum = 0

    for line in fdin:
        reverse_line = line[::-1]
        auxiliar_line = line
        
        reverse_line = re.sub(r"eno|owt|eerht|ruof|evif|xis|neves|thgie|enin", transformrev, reverse_line)
        auxiliar_line = re.sub(r"one|two|three|four|five|six|seven|eight|nine", transform, auxiliar_line)

        first_number = 0
        second_number = 0

        for char in auxiliar_line:
            if char.isdigit():
                first_number = int(char)
                break

        for char in reverse_line:
            if char.isdigit():
                second_number = int(char)
                break

        final_number = (first_number * 10) + second_number
        total_sum += final_number

    return total_sum


print(trebuchet(fdin))