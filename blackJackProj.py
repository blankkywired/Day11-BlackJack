import random
import os

import drawLogo
#Notes
#Ace/Às: 1 or 11
#Jack: 10
#Queen: 10
#King: 10

choosenCardsDealer = []
choosenCardsOwner = []
limiter = 21
totalScoreUser = []
totalScoreDealer = []
def choice_card_function(quantity, owner):
    amountTotalUser = 0 #Acumulador dos valores de cada carta do  usuario
    amountValueDealer = 0 #Acumulador dos valores de cada carta do computador(dealer)

    cardsValueList = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "K", "Q"]
    if owner == "user":
        for i in range(quantity):
            choosenCards = (random.choice(cardsValueList))
            choosenCardsOwner.append(choosenCards)
        for card in choosenCardsOwner:
            if card == "J" or card == "K" or card == "Q":
                amountTotalUser += 10
            elif card == "A":
                amountTotalUser += int(input('What value do you want?(1/11):'))
            else:
                amountTotalUser += card
        totalScoreUser.append(amountTotalUser) #Salvando o valor total em totalScoreUser
        return f"Your cards {choosenCardsOwner} Total Score {amountTotalUser}"

    elif owner == "dealer":
        for i in range(quantity):
            choosenCards = (random.choice(cardsValueList))
            choosenCardsDealer.append(choosenCards)
        for card in choosenCardsDealer:
            if card == "J" or card == "K" or card == "Q":
                amountValueDealer += 10
            else:
                amountValueDealer += card
            totalScoreDealer.append(amountValueDealer)
        return f"Computer  {choosenCardsDealer}, Total Score: {amountValueDealer} , computer first card: {choosenCardsDealer[0]}"

def main():
    print(drawLogo.logo)
    firstChoice = input("Do you want to play a blackjack game? 'Y' or 'N': ").capitalize()
    if firstChoice == "Y":
        print(f'\n{choice_card_function(quantity=2, owner='user')}')
        print(f'{choice_card_function(quantity=2, owner='dealer')}')

    condiction = True
    while condiction:

            #print(f'Pontos totais {totalScoreUser[-1]}')
            if totalScoreUser[-1] < limiter :
                choice = input("Type 'y' to get another card or type 'n' to pass: ").capitalize()

                if choice == "Y": #Buy a card
                    print(choice_card_function(1, 'user'))
                elif choice == "N": #Pass
                    print(choice_card_function(1, 'dealer'))
                    if totalScoreDealer[-1] > limiter:
                        print(f"You win: Computer's final hand{choosenCardsDealer}")
                        condiction = False
                        break
                    elif totalScoreDealer[-1] == limiter:
                        print(f"You lose\nComputer's final hand{choosenCardsDealer} Computer final socre: {totalScoreDealer[-1]}")
                        condiction = False
                    else:
                         print(f"You win: Computer's final hand{choosenCardsDealer}")
                         condiction = False

            elif totalScoreUser[-1] > limiter:
                print('You lose')
                print(f"Computer's final hand{choosenCardsDealer} Computer final score: {totalScoreDealer[-1]}")
                break
            else:
                print(f"You win {choosenCardsOwner} Your Score {totalScoreUser[-1]}\nComputer's final hand:{choosenCardsDealer}")

while True:

    choosenCardsDealer = []
    choosenCardsOwner = []
    limiter = 21
    totalScoreUser = []
    totalScoreDealer = []
    main()

#Adicionado linha de test
