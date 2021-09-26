from tools import *
from Decks.Virtual_World.vw_sets import *
from common_sets import *

def vw_hand_is_combo(hand, deck, desires, prosperity):
    combo = False
    through_nib = False
    through_ash = False
    hts = 0
    hts = playable_hts_in_hand(hand)
    lvl3 = cards_of_set_in_hand(hand, vw_lvl3)
    lvl6 = cards_of_set_in_hand(hand, vw_lvl6)
    extenders = cards_of_set_in_hand(hand, vw_extenders)

    if not desires and not prosperity: #if desires or prosperity it means that comboing without them was not possible, thus ash beats the hand
        through_ash = hand_through_ash(deck, hand)
    else: through_ash = False

    if lvl3 >= 2:
        combo = True
    if lvl3 == 1 and not combo:
        if lvl6 >= 1:
            combo = True
        elif extenders >= 1:
            combo = True
        elif in_hand(hand,"Virtual World Mai-Hime - Lulu") and in_hand(hand, "Virtual World Gate - Qinglong"):
            combo = True
    if lvl3 == 0 and not combo:
        if lvl6 >= 1 and extenders >= 1:
            combo = True
        elif in_hand(hand,"Virtual World Kirin - Lili") and in_hand(hand, "Virtual World Gate - Qinglong"):
            combo = True
    
    if in_hand(hand, "Pot of Desires") and not desires and not prosperity and combo:
        deck, hand = pot_of_desires(deck, hand)
        through_ash = hand_through_ash(deck, hand)
        desires = True
    if in_hand(hand, "Pot of Prosperity") and not desires and not prosperity and combo:
        deck, hand, chosen = pot_of_prosperity(deck, hand)
        if chosen:
            through_ash = hand_through_ash(deck, hand)
        prosperity = True
    
    if in_hand(hand, "Pot of Prosperity") and not desires and not prosperity and not combo:
        deck, hand, chosen = pot_of_prosperity(deck, hand)
        if not chosen: return combo, hts, through_nib, through_ash
        return vw_hand_is_combo(hand, deck, desires, prosperity=True)

    if in_hand(hand, "Upstart Goblin") and not prosperity and not combo:
        hand, deck = upstart_goblin(hand, deck)
        return vw_hand_is_combo(hand, deck, desires, prosperity=True)

    if in_hand(hand, "Pot of Desires") and not desires and not prosperity and not combo:
        deck, hand = pot_of_desires(deck, hand)
        return vw_hand_is_combo(hand, deck, desires=True, prosperity=prosperity)

    return combo, hts, through_nib, through_ash

def hand_through_ash(deck, hand):
    ash = False
    diff_lvl3 = different_cards_of_set_in_hand(hand, vw_lvl3)
    diff_lvl6 = different_cards_of_set_in_hand(hand, vw_lvl6)
    extenders = cards_of_set_in_hand(hand, vw_extenders)
    if diff_lvl3 + diff_lvl6 >=3:
        return True
    if diff_lvl3>=2 and extenders >= 1:
        return True
    if diff_lvl3>=1 and diff_lvl6 and extenders >= 1:
        return True
    if in_hand(hand, "Called by the Grave"):
        return True
    if in_hand(hand, "Upstart Goblin"):
        hand, deck = upstart_goblin(hand, deck)
        hand_through_ash(deck, hand)
    return ash
    
def pot_of_prosperity(deck, hand):
    hand.remove("Pot of Prosperity")
    tmp_deck = deck
    draws, tmp_deck = draw(tmp_deck, 6)
    chosen = False
    for card in draws:
        if card in vw_lvl3:
            hand.append(card)
            chosen = True
            break
    if not chosen:
        for card in draws:
            if card in vw_lvl6:
                hand.append(card)
                chosen = True
                break
    if not chosen:
        for card in draws:
            if card in vw_extenders:
                hand.append(card)
                chosen = True
                break
    return deck, hand, chosen

    # not true because no more normal summon
    # if in_hand(hand, "Virtual World Hime - Nyannyan") and in_hand(hand, "Emergency Teleport") and not prosperity:
    #     hand.remove("Virtual World Hime - Nyannyan")
    #     hand.remove("Emergency Teleport")
    #     draws, deck = draw(deck, 1)
    #     for card in draws:
    #         hand.append(card)
    #     if vw_hand_is_combo(hand, deck, desires, prosperity=True)[0]:
    #         print(hand)
    #     return vw_hand_is_combo(hand, deck, desires, prosperity)

    #manque le cas si prospe et desires et pas combo avant pour ash