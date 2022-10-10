import random

deck = [
    'AH','2H','3H','4H','5H','6H','7H','8H','9H','TH','JH','QH','KH',
    'AD','2D','3D','4D','5D','6D','7D','8D','9D','TD','JD','QD','KD',
    'AS','2S','3S','4S','5S','6S','7S','8S','9S','TS','JS','QS','KS',
    'AC','2C','3C','4C','5C','6C','7C','8C','9C','TC','JC','QC','KC'
]



random.shuffle(deck)



player_hand = []
dealer_hand = []

dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())







player_hand_value = 0
dealer_hand_value = 0

for card in player_hand:
    if card[0] == 'A':
        player_hand_value += 1
    elif card[0] == '2':
        player_hand_value += 2
    elif card[0] == '3':
        player_hand_value += 3
    elif card[0] == '4':
        player_hand_value += 4
    elif card[0] == '5':
        player_hand_value += 5
    elif card[0] == '6':
        player_hand_value += 6
    elif card[0] == '7':
        player_hand_value += 7
    elif card[0] == '8':
        player_hand_value += 8
    elif card[0] == '9':
        player_hand_value += 9
    elif card[0] == 'T':
        player_hand_value += 10
    elif card[0] == 'J':
        player_hand_value += 10
    elif card[0] == 'Q':
        player_hand_value += 10
    elif card[0] == 'K':
        player_hand_value += 10
    
for card in dealer_hand:
    if card[0] == 'A':
        dealer_hand_value += 1
    elif card[0] == '2':
        dealer_hand_value += 2
    elif card[0] == '3':
        dealer_hand_value += 3
    elif card[0] == '4':
        dealer_hand_value += 4
    elif card[0] == '5':
        dealer_hand_value += 5
    elif card[0] == '6':
        dealer_hand_value += 6
    elif card[0] == '7':
        dealer_hand_value += 7
    elif card[0] == '8':
        dealer_hand_value += 8
    elif card[0] == '9':
        dealer_hand_value += 9
    elif card[0] == 'T':
        dealer_hand_value += 10
    elif card[0] == 'J':
        dealer_hand_value += 10
    elif card[0] == 'Q':
        dealer_hand_value += 10
    elif card[0] == 'K':
        dealer_hand_value += 10 

print(f"Your hand is {player_hand[0]} and {player_hand[1]}")
print(f"The dealer's hand is {dealer_hand[0]} and Hidden")

change_ace_value = False

for card in player_hand:
    if card[0] == 'A':
        while change_ace_value == False:
            change_ace_answer = input('Would you like your ace to be worth 1 or 11?')
            if change_ace_answer == '11':
                player_hand_value += 10
                change_ace_value = True
            elif change_ace_answer == '1':
                change_ace_value = True
            else:
                print('Sorry, invalid input.')



print(f"Your total is {player_hand_value}")
player_answer = input("Wolud you like to Hit(h) or Stand(s)?")
if player_answer == "h":
    
    print("You hit")
elif player_answer == "s":
    print("You stand")
else:
    print()

if player_hand_value > 21:
    print("You Lose!")
else:
    print("You Win")


