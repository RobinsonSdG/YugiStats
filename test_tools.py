import sys
from Decks.Virtual_World.vw_sets import *
from tools import *

hand_3playable_hts = ["Nibiru, the Primal Being", "Effect Veiler", "Fantastical Dragon Phantazmay", "Dragon Buster Destruction Sword", "Dragon Buster Destruction Sword"]
hand_2playable_hts = ["Nibiru, the Primal Being", "Nibiru, the Primal Being", "Fantastical Dragon Phantazmay", "Fantastical Dragon Phantazmay", "Dragon Buster Destruction Sword"]
hand_3lvl3vw = ["Virtual World Mai-Hime - Lulu", "Virtual World Xiezhi - Jiji", "Virtual World Xiezhi - Jiji", "Virtual World Kirin - Lili", "Virtual World Roshi - Laolao"]
def test_playable_hts_in_hand():
    assert playable_hts_in_hand(hand_3playable_hts) == 3
    assert playable_hts_in_hand(hand_2playable_hts) == 2

def test_cards_of_set_in_hand():
    assert cards_of_set_in_hand(hand_3lvl3vw, vw_lvl3) == 3

