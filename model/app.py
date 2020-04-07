from random import choice, shuffle

cards_values = {
'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10
}

cards = 8 * ['A','2','3','4','5','6','7','8','9','10','J','Q', 'K']

#UTILS
def show_options():
    print('1 - Hit a card')
    print('2 - Hold')
    print('3 - Finish the game')

def show_score():
    print(f'Player {player_score}x{dealer_score} Dealer')

def show_game_score():
    print(f'Player {player_score}x{dealer_game_score} Dealer')

def getPoints(hand):
    sum = 0
    for card in hand:
        sum += cards_values[card]
    return sum

def show_hands(hand):
    print(f'Hand: {[x for x in hand]}', sep='  ')

def obtain_random_card():
    shuffle(cards)
    return choice(cards)

#main
dealer_game_score = 0
player_game_score = 0

dealer_score = 0
player_score = 0

player_hand = []
dealer_hand = []

option = 1
round = 0
round_finished = False
while getPoints(player_hand) < 21 and getPoints(dealer_hand) < 21 and round_finished == False:
    round = round + 1
    print(f'\n\n*********** R O U N D   {round}  **************\n')

    while option == 1:
        player_hand.append(obtain_random_card())
        show_hands(player_hand)
        player_score = getPoints(player_hand)
        print(f'player_score: {player_score}\n\n')
        show_options()
        option = input('\nOption: ')

        if player_score > 21:
            round_finished = True

    while option == 2 and round_finished == False:
        dealer_hand.append(obtain_random_card())
        show_hands(dealer_hand)
        dealer_score = getPoints(dealer_hand)

        if dealer_score > player_score and dealer_score < 21:
            round_finished = True

        print(f'Dealer score: {dealer_score}\n\n')

    if option == 3:
        round_finished = True
        print('FIM DE JOGO')
        print(show_game_score())

























