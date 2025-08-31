import random
import drawLogo
print(drawLogo.logo)
3
def deaf_card():
    """Choice a random card of the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards = random.choice(cards)
    return cards


def total_score(owner):
    total = sum(owner)
    if 11 in owner and total > 21:
        owner.remove(11)
        owner.append(1)
        total = sum(owner)
    return total


def find_winner():
    user = total_score(user_cards)
    dealer = total_score(computer_cards)

    if user > 21:
        return "Dealer wins! Player busted."
    elif dealer > 21:
        return "Player wins! Dealer busted."
    elif user == dealer:
        return "Draw!"
    elif user == 21:
        return "Player wins with Blackjack!"
    elif dealer == 21:
        return "Dealer wins with Blackjack!"
    elif user > dealer:
        return "Player wins!"
    else:
        return "Dealer wins!"
    
user_cards = []
computer_cards = []

#First move
for i in range(2):
    user_cards.append(deaf_card())
    computer_cards.append(deaf_card())

#Show result of the first move
print(f'User Hand {user_cards} Current score: {total_score(user_cards)}\nComputer first card: {computer_cards[0]}')

while total_score(user_cards) < 21:
    continue_to_play = input("Type 'y' to get another card or press n 'to' pass: ")
    if continue_to_play == "y":
        user_cards.append(deaf_card())
        print(f'User Hand {user_cards} Current score: {total_score(user_cards)}\nComputer first card: {computer_cards[0]}')
    else:
        break
while total_score(computer_cards) < 17:
    computer_cards.append(deaf_card())
print(f'User Hand {user_cards} Current score: {total_score(user_cards)}\nComputer final hand: {computer_cards} Total Score: {total_score(computer_cards)}')
print(find_winner())


