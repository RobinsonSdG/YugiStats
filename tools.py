from common_sets import *
import random

# Shuffles deck
def shuffle(deck):
    random.shuffle(deck)

# Draws n cards
def draw(deck, n):
    hand = []
    test_deck = deck.copy()
    shuffle(test_deck)
    for i in range(n):
        hand.append(test_deck.pop(0))
    return hand, test_deck

# Checks if we have a specific card in hand
def in_hand(hand, card):
    return card in hand

# Checks if we have a handtrap in hand
def hts(hand):
    return any(i in handtraps for i in hand)

def playable_hts_in_hand(hand):
    nb_hts = 0
    temp_hand_hts = []
    for card in hand:
        if card in handtraps and card not in opt_handtraps:
            nb_hts += 1
            temp_hand_hts.append(card)
        elif card in opt_handtraps and card not in temp_hand_hts:
            nb_hts += 1
            temp_hand_hts.append(card)
    return nb_hts

def cards_of_set_in_hand(hand, card_set):
    number_card_of_set_in_hand = 0
    for card in card_set:
        number_card_of_set_in_hand += hand.count(card)
    return number_card_of_set_in_hand

def different_cards_of_set_in_hand(hand, card_set):
    number_card_of_set_in_hand = 0
    diff = 0
    for card in card_set:
        number_card_of_set_in_hand += hand.count(card)
        if in_hand(hand, card):
            diff += 1
    return number_card_of_set_in_hand

def triple_tactics_talent(deck, hand):
    hand.remove("Triple Tactics Talent")
    draws, deck = draw(deck, 2)
    for card in draws:
        hand.append(card)
    return deck, hand

def pot_of_desires(deck, hand):
    hand.remove("Pot of Desires")
    for i in range(10):
        deck.pop()
    draws, deck = draw(deck, 2)
    for card in draws:
        hand.append(card)
    return deck, hand

def upstart_goblin(hand, deck):
    hand.remove("Upstart Goblin")
    draws, deck = draw(deck, 1)
    for card in draws:
        hand.append(card)
    return hand, deck
    
