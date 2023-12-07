import re
import time

time_start = time.time()

fdin = open("input.txt")

def scratchcards(fdin):

    fdin = fdin.read().splitlines()
    card_instances = [0] * (len(fdin) + 1)

    total_points = 0

    for line in fdin:

        game_id, cards = line.split(':')
        winning_numbers, my_numbers = cards.split('|')

        game_id = int(game_id.split()[-1])
        winning_numbers = re.findall(r"\d+", winning_numbers)
        my_numbers = re.findall(r"\d+", my_numbers)

        card_instances[game_id] += 1
        current_winning_sum = 0
        current_points = 0

        for number in my_numbers:
            if number in winning_numbers:
                current_points = 2**current_winning_sum
                current_winning_sum += 1

        
        if current_winning_sum > 0:
            for i in range(game_id + 1, game_id + current_winning_sum + 1):
                card_instances[i] += card_instances[game_id]

        total_points += current_points
        
            
    return total_points, sum(card_instances)


part_one_result, part_two_result = scratchcards(fdin)
time_end = time.time()
print(f"Part One Result: {part_one_result}, Part Two Result: {part_two_result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")