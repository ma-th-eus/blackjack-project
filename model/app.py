from random import choice, shuffle
import logging
import pytest

logging.basicConfig(filename="log.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
#Creating an object
logger=logging.getLogger()
#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

cards_values = {
'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10
}

cards = 8 * ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

#UTILS
def show_options():
    print('1 - Hit a card')
    print('2 - Hold')
    print('3 - Finish the game')

def show_score():
    print(f'        ROUND SCORE       ')
    print(f'*** Player {player_round_score}x{dealer_round_score} Dealer ***')

def show_game_score():
    print(f'__GAME SCORE__')
    print(f'Player {player_game_score}x{dealer_game_score} Dealer')

def show_game_score_final():
    winner = 'Player' if player_game_score > dealer_game_score else 'Dealer'
    print('--------------FINAL SCORE------------------------------------------')
    print(f'Player {player_game_score}x{dealer_game_score} Dealer')
    print(f'Congratz! {winner}')
    print('-------------------------------------------------------------------')


def getPoints(hand):
    sum = 0
    for card in hand:
        sum += cards_values[card]
    return sum

def show_hands(hand):
    print(f'Hand: {[x for x in hand]}', sep='  ')

def obtain_random_card():
    shuffle(cards)
    card = choice(cards)
    cards.remove(card)
    return card

def refresh_cards():
    cards = 8 * ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    shuffle(cards)
    shuffle(cards)
    return cards

def check_round_winner(p_score, d_score):
    print('Entrou no check_round_winner')
    if p_score > 21:
        print('D1')
        return 'Dealer'

    elif p_score == 21:
        print('P1')
        return 'Player'
    else:
        if d_score > 21:
            print('P2')
            return 'Player'
        if p_score == d_score:
            print('D2 - draw')
            return 'Dealer'

        if d_score <= 21:
            if d_score >= p_score:
                print('D3')
                return'Dealer'
            else:
                print('P3')
                return 'Player'

    print('Error')
    return 'Dealer'


#main
dealer_game_score = 0
player_game_score = 0

round = 0
# round_finished = False
game_finished = False


while game_finished == False and round < 10:
    player_hand = []
    dealer_hand = []
    option = 1
    dealer_round_score = 0
    player_round_score = 0
    round_finished = False
    refresh_cards()
    print(f'\n\n*********** R O U N D   {round + 1}  ************** - len cards: {len(cards)}\n')

    while option == 1 and round_finished == False:
        # print(player_round_score, '  ', round_finished)
        player_hand.append(obtain_random_card())
        show_hands(player_hand)
        player_round_score = getPoints(player_hand)
        print(f'player round score: {player_round_score}\n\n')
        if player_round_score < 21:
            show_options()
            option = int(input('\nOption: '))
        else:
            round_finished = True


    while option == 2 and dealer_round_score < player_round_score and round_finished == False:
        dealer_hand.append(obtain_random_card())
        show_hands(dealer_hand)
        dealer_round_score = getPoints(dealer_hand)

        if dealer_round_score > 21 or dealer_round_score >= player_round_score:
            round_finished = True

        print(f'Dealer round score: {dealer_round_score}\n\n')

    if option == 3:
        round_finished = True
        print('FIM DE JOGO')
        game_finished = False
        print(show_game_score())

    if round_finished == True and game_finished == False:
        if check_round_winner(player_round_score, dealer_round_score) == 'Dealer':
            print('Dealer wins!')
            dealer_game_score += 1
        # elif check_round_winner(dealer_round_score, player_round_score) == 'Player':
        else:
            print('Player wins!')
            player_game_score += 1


    elif option > 3:
        print('Invalid option!')

    show_score()
    round = round + 1
    show_game_score()

show_game_score_final()



























