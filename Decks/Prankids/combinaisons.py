from tools import *
from Decks.Prankids.pk_sets import *
from common_sets import *

def pk_hand_is_combo(hand, deck, desires, prosperity):
    combo = False
    through_nib = False
    through_ash = False
    hts = 0
    hts = playable_hts_in_hand(hand)
    pks = cards_of_set_in_hand(hand, pk_monsters)
    if pks >= 1:
        combo = True

    if in_hand(hand, "Pot of Desires") and not desires and not prosperity:
        hand.remove("Pot of Desires")
        for i in range(10):
            deck.pop()
        draws, deck = draw(deck, 2)
        for card in draws:
            hand.append(card)
        return pk_hand_is_combo(hand, deck, desires=True, prosperity=prosperity)
    return combo, hts, through_nib, through_ash