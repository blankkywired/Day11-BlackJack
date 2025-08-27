import random
import drawLogo
print(drawLogo.logo)
def deaf_card():
    """Choice a random card of the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards = random.choice(cards)
    return cards

def total_score(owner):
    """Sum the total value of the owner's hand"""
    sumNum = 0
    for element in owner:
        sumNum += element
    return sumNum


def find_winner():
    """Find the final winner using value's total score"""

    if total_score(user_cards) == 21 and total_score(computer_cards) != 21:
        return "Player wins"
    elif total_score(user_cards) > 21:
        return "Dealer Wins"
    elif total_score(user_cards) == 21 and total_score(computer_cards) == 21:
        return "Draw"
    elif 0 < total_score(user_cards) <= 21 and total_score(computer_cards) > 21:
        return "Player wins" 
    elif total_score(user_cards) < (total_score(computer_cards) < 21):
        return "Dealer wins"
    elif total_score(user_cards) < 21 and total_score(computer_cards) == 21:
        return "Dealer Wins"
    


user_cards = []
computer_cards = []


for i in range(2):
    user_cards.append(deaf_card())
    computer_cards.append(deaf_card())

#print(f'User Hand {user_cards} Total: {total_score(user_cards)}\nComputer Hand{computer_cards} Total: {total_score(computer_cards)}')
print(f'User Hand {user_cards} Current score: {total_score(user_cards)}\nComputer current score {total_score(computer_cards)}')

condition = True
while condition:
    if total_score(computer_cards) < 17:
        continueToPlay = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    
        if continueToPlay == "y":
            for i in range(1):
                user_cards.append(deaf_card())
                computer_cards.append(deaf_card())
        elif continueToPlay == "n":
            computer_cards.append(deaf_card())
    else:
        continueToPlay = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if continueToPlay == "y":
            for i in range(1):
                user_cards.append(deaf_card())
                computer_cards.append(deaf_card())
        elif continueToPlay == "n":
            computer_cards.append(deaf_card())
    condition = False

print(f'User Hand {user_cards} Current score: {total_score(user_cards)}\nComputer hand: {computer_cards} Total Score: {total_score(computer_cards)}')
print(find_winner())


