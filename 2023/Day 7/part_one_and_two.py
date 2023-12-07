import time

time_start = time.time()

GAMES = (open("input.txt")).read().splitlines()
CARD_STRENGTH_PART_ONE = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARD_STRENGTH_PART_TWO = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

# Types:
#
# 1 -> High Card
# 2 -> One Pair
# 3 -> Two Pair
# 4 -> Three Of A Kind
# 5 -> Full House
# 6 -> Four Of A Kind
# 7 -> Five Of A Kind
#
#
# Hand Tuple -> (Hand, Bet, Type)


def camel_cards():
    global GAMES

    new_hands_part_one = []
    new_hands_part_two = []
    card_count_part_one = []
    card_count_part_two = []
    total_winnings_part_one = 0
    total_winnings_part_two = 0

    for index, game in enumerate(GAMES):

        card_count_part_one.append(dict())
        card_count_part_two.append(dict())
        current_hand, current_bet = game.split()

        for current_card in current_hand:
            if current_card in card_count_part_one[index]:
                card_count_part_one[index][current_card] += 1
                card_count_part_two[index][current_card] += 1

            else:
                card_count_part_one[index][current_card] = 1
                card_count_part_two[index][current_card] = 1

        card_count_part_one[index] = dict(sorted(card_count_part_one[index].items(), key=lambda x:x[1], reverse=True))
        card_count_part_two[index] = dict(sorted(card_count_part_two[index].items(), key=lambda x:x[1], reverse=True))
        unique_cards_part_one = list(card_count_part_one[index])
        unique_cards_part_two = list(card_count_part_two[index])

        if 'J' in unique_cards_part_two:
            unique_cards_part_two.remove('J')

            if len(unique_cards_part_two) == 0:
                card_count_part_two[index]['A'] = 5

            else:
                card_count_part_two[index][unique_cards_part_two[0]] += card_count_part_two[index]['J']


        match (len(unique_cards_part_one)):
            case 1:
                new_hands_part_one.append((current_hand, current_bet, 7))

            case 2:
                if card_count_part_one[index][unique_cards_part_one[0]] == 4:
                    new_hands_part_one.append((current_hand, current_bet, 6))

                else:
                    new_hands_part_one.append((current_hand, current_bet, 5))
            
            case 3:
                if card_count_part_one[index][unique_cards_part_one[0]] == 3:
                    new_hands_part_one.append((current_hand, current_bet, 4))

                else:
                    new_hands_part_one.append((current_hand, current_bet, 3))
            
            case 4:
                new_hands_part_one.append((current_hand, current_bet, 2))


            case 5:
                new_hands_part_one.append((current_hand, current_bet, 1))

        
        match (len(unique_cards_part_two)):
            case 0:
                new_hands_part_two.append((current_hand, current_bet, 7))
            case 1:
                new_hands_part_two.append((current_hand, current_bet, 7))

            case 2:
                if card_count_part_two[index][unique_cards_part_two[0]] == 4:
                    new_hands_part_two.append((current_hand, current_bet, 6))

                else:
                    new_hands_part_two.append((current_hand, current_bet, 5))
            
            case 3:
                if card_count_part_two[index][unique_cards_part_two[0]] == 3:
                    new_hands_part_two.append((current_hand, current_bet, 4))

                else:
                    new_hands_part_two.append((current_hand, current_bet, 3))
            
            case 4:
                new_hands_part_two.append((current_hand, current_bet, 2))


            case 5:
                new_hands_part_two.append((current_hand, current_bet, 1))


    new_hands_part_one.sort(key=lambda hand: (hand[2], *[CARD_STRENGTH_PART_ONE.index(card) for card in hand[0]]))
    new_hands_part_two.sort(key=lambda hand: (hand[2], *[CARD_STRENGTH_PART_TWO.index(card) for card in hand[0]]))

    for index, new_hand in enumerate(new_hands_part_one):

        total_winnings_part_one += int(new_hand[1]) * (index + 1)

    
    for index, new_hand in enumerate(new_hands_part_two):

        total_winnings_part_two += int(new_hand[1]) * (index + 1)

    
    return total_winnings_part_one, total_winnings_part_two



part_one_result, part_two_result = camel_cards()
time_end = time.time()
print(f"Part One Result: {part_one_result}, Part Two Result: {part_two_result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")