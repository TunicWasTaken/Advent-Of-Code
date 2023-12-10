import re
import time

time_start = time.time()

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


result = scratchcards(fdin)
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")