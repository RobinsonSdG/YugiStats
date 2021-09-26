from tools import *
from Decks.Prankids.pk_sets import *
from common_sets import *

def pk_hand_is_combo(hand, deck, desires, prosperity):
    combo = False
    through_nib = False
    through_ash = False
    hts = 0
    nb_interupts = 0
    nb_interupts = cards_of_set_in_hand(hand, interupts)
    hts = playable_hts_in_hand(hand)
    pks = cards_of_set_in_hand(hand, pk_monsters)
    if not desires and not prosperity: #if desires or prosperity it means that comboing without them was not possible, thus ash beats the hand
        through_ash = hand_through_ash(deck, hand)
    else: through_ash = False

    if pks >= 1:
        combo = True

    if in_hand(hand, "Pot of Desires") and not desires and not prosperity and combo and not through_ash:
        deck, hand = pot_of_desires(deck, hand)
        through_ash = hand_through_ash(deck, hand)
        desires = True

    if in_hand(hand, "Pot of Desires") and not desires and not prosperity and not combo:
        deck, hand = pot_of_desires(deck, hand)
        return pk_hand_is_combo(hand, deck, desires=True, prosperity=prosperity)

    return combo, hts, through_nib, through_ash, nb_interupts

def hand_through_ash(deck, hand):
    ash = False
    diff_monsters = different_cards_of_set_in_hand(hand, pk_monsters)
    pks = cards_of_set_in_hand(hand, pk_monsters)
    sextenders = cards_of_set_in_hand(hand, super_extenders)
    fusions = cards_of_set_in_hand(hand, fusion)
    ah = cards_of_set_in_hand(hand, anti_hts)
    if in_hand(hand, ah):
        return True
    if (in_hand(hand, "Polymerization") or in_hand(hand, "Prank-Kids Pandemonium")) and pks >=2:
        return True
    if pks >= 1 and sextenders>=1:
        return True
    if pks >= 2 and in_hand(hand, "Prank-Kids Pranks"):#ajouter une carte prankids
        return True

    # if in_hand(hand, "Triple Tactics Talent"):
    #     deck, hand = triple_tactics_talent(deck, hand)
    #     return hand_through_ash(deck, hand)
    if in_hand(hand, "Upstart Goblin"):
        hand, deck = upstart_goblin(hand, deck)
        hand_through_ash(deck, hand)
    return ash