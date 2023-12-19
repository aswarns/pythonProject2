# 720720-7957 RSBrothers KPHB

#

import sys
import random

# Step 1 - Set contants and ask for bet

HEARTS = chr(9829)  # Charater is ♥
DIAMONDS = chr(9830)  # Charater is ♦
SPADES = chr(9824)  # Charater is ♠
CLUBS = chr(9827)  # Charater is ♣
BACKSIDE = 'backside'

print("Welcome to BlackJack")
money = 5000

# Step2 - get bet function


def get_bet(maxBet):
    """Ask the plaer how money they want to bet for this round"""
    while True:
        print("How much do you bet? (1-{}, or QUIT)".format(maxBet))
        bet = input("> ").upper().strip()
        if bet == "QUIT" or bet == "q":
            print("Thanks for playing!")
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


# Step3 - Get Deck
def get_deck():
    """Return a list of tuple (rank, suit) for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            # add the number of cards
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            # add face and ace cards
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


# Step4 - display cards
def display_cards(cards):
    """ Display all the cards in the card list"""
    rows = ['', '', '', '', '']
    for card in cards:
        rows[0] += ' ___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[1] += '|###| '
            rows[1] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, "_"))
    for row in rows:
        print(row)


# step5 - Gte Hand value
def get_hand_value(cards):
    "Return value of cards."
    value = 0
    number_aces = 0
    # Add the value for non ace cards.
    for card in cards:
        rank = card[0]
        if rank == "A":
            number_aces += 1
        elif rank in ('K', 'J', 'Q'):
            value += 10
        else:
            value += int(rank)
    value += number_aces
    for i in range(number_aces):
        # If another 10 can be added without busting
        if value + 10 <= 21:
            value += 10
    return value


# Step 6 - Display hands
def display_hands(player_hand, dealer_hand, show_dealer_hand):
    """Show player and dealer hand"""
    print()
    if show_dealer_hand:
        print("DEALER ", get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print("DEALER: ???")
        # Hide dealer's first Hand
        display_cards([BACKSIDE] + dealer_hand[1:])
    # Show the player's card
    print("PLAYER: ", get_hand_value(player_hand))
    display_cards(player_hand)


# Step 7 - Get move
def get_move(player_hand, money):
    """Ask the player for thier move, rerurn H, S or D"""
    while True:
        # Determone what move the player can moke
        moves = ["(H)it", "(S)tand"]
        if len(player_hand) == 2 and money > 0:
            moves.append('(D)ouble down')
        # Ask from plaer the mce, by showing options
        move_prompt = ', '.join(moves) + '>'
        move = input(move_prompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move


# main program
while True:
    # Check ifplaer has run out of money
    if money <= 0:
        print("It is good that we weren't playing with real money.")
        print("Thanks for playing.")
        sys.exit()
    # Ask PLayer to enter thier money
    print("Money: ", money)
    # Get bet
    bet = get_bet(money)
    # Get Deck
    deck = get_deck()
    # GIve the dealyer and plaer two cards from the deck
    dealer_hand = [deck.pop(), deck.pop()]
    player_hand = [deck.pop(), deck.pop()]
    # Handle player actions
    print('Bet: ', bet)

    while True:
        display_hands(player_hand, dealer_hand, False)
        print()
        # Check if player has bust
        if get_hand_value(player_hand) > 21:
            break
        # Get player's move
        move = get_move(player_hand, money - bet)
        # Handle player moves
        if move == 'D':
            # Increase the bet
            additional_bet = get_bet(min(bet, (money-bet)))
            bet += additional_bet
            print("Bet increased to {}.".format(bet))
            print('Bet:', bet)
        if move in ('H', 'D'):
            # Get another card
            new_card = deck.pop()
            rank, suit = new_card
            print(f"You drew a {rank} of {suit}.")
            player_hand.append(new_card)
            # Check if player has bust
            if get_hand_value(player_hand) > 21:
                continue
        if move == 'S':
            # Stops player's turn
            break
    # Handle dealer's actions
    if get_hand_value(player_hand) <= 21:
        while get_hand_value(dealer_hand) < 17:
            # The dealer hits
            print("The dealer hits..")
            dealer_hand.append(deck.pop())
            display_hands(player_hand, dealer_hand, False)
            if get_hand_value(dealer_hand) > 21:
                # The dealer has busted
                break
            input("Press enter to continie..")
            print('\n\n')

    display_hands(player_hand, dealer_hand, True)
    player_value = get_hand_value(player_hand)
    dealer_value = get_hand_value(dealer_hand)
    # Handle whether the player won, lost or draw
    if dealer_value > 21:
        print(f"Dealer busts! You win ${bet}!")
        money += bet
    elif player_value > 21 or player_value < dealer_value:
        print("You lost!")
        money -= bet
    elif player_value > dealer_value:
        print(f"You win ${bet}!")
        money += bet
    elif player_value == dealer_value:
        print("It is a draw and the bet is returned to you!")
    input("Press enter to continue..")
    print('\n\n')
