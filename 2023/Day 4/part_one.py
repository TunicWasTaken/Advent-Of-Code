import re

fdin = open("input.txt")

def scratchcards(fdin):

    total_points = 0

    for line in fdin:

        cards = line.split(':')[1]
        winning_numbers, my_numbers = cards.split('|')

        winning_numbers = re.findall(r"\d+", winning_numbers)
        my_numbers = re.findall(r"\d+", my_numbers)
        
        current_points = 0
        current_winning_sum = 0

        for number in my_numbers:
            if number in winning_numbers:
                current_points = 2**current_winning_sum
                current_winning_sum += 1

        
        total_points += current_points
    
    return total_points


print(scratchcards(fdin))