import time

time_start = time.time()

GAMES = (open("input.txt")).read().splitlines()
CARD_STRENGTH = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

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

    new_hands = []
    card_count = []
    total_winnings = 0

    for index, game in enumerate(GAMES):

        card_count.append(dict())
        current_hand, current_bet = game.split()

        for current_card in current_hand:
            if current_card in card_count[index]:
                card_count[index][current_card] += 1

            else:
                card_count[index][current_card] = 1

        card_count[index] = dict(sorted(card_count[index].items(), key=lambda x:x[1], reverse=True))
        unique_cards = list(card_count[index])
        
        match (len(unique_cards)):
            case 1:
                new_hands.append((current_hand, current_bet, 7))

            case 2:
                if card_count[index][unique_cards[0]] == 4:
                    new_hands.append((current_hand, current_bet, 6))

                else:
                    new_hands.append((current_hand, current_bet, 5))
            
            case 3:
                if card_count[index][unique_cards[0]] == 3:
                    new_hands.append((current_hand, current_bet, 4))

                else:
                    new_hands.append((current_hand, current_bet, 3))
            
            case 4:
                new_hands.append((current_hand, current_bet, 2))


            case 5:
                new_hands.append((current_hand, current_bet, 1))


    new_hands.sort(key=lambda hand: (hand[2], *[CARD_STRENGTH.index(card) for card in hand[0]]))
    
    for index, new_hand in enumerate(new_hands):

        total_winnings += int(new_hand[1]) * (index + 1)

    
    return total_winnings



result = camel_cards()
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")