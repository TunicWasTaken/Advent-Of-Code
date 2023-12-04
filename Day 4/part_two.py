import re

fdin = open("input.txt")

def scratchcards(fdin):

    fdin = fdin.read().splitlines()
    card_instances = [0] * (len(fdin) + 1)

    for line in fdin:

        game_id, cards = line.split(':')
        winning_numbers, my_numbers = cards.split('|')

        game_id = int(game_id.split()[-1])
        winning_numbers = re.findall(r"\d+", winning_numbers)
        my_numbers = re.findall(r"\d+", my_numbers)

        card_instances[game_id] += 1
        current_winning_sum = 0

        for number in my_numbers:
            if number in winning_numbers:
                current_winning_sum += 1

        
        if current_winning_sum > 0:
            for i in range(game_id + 1, game_id + current_winning_sum + 1):
                card_instances[i] += card_instances[game_id]

            
    return sum(card_instances)


print(scratchcards(fdin))