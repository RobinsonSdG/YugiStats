import random
from Decks.Virtual_World.combinaisons import vw_hand_is_combo
from Decks.Prankids.combinaisons import pk_hand_is_combo
from tools import *
from progress.bar import *
import time

# Keeps track of numbers times we can successfully FTK
def combo_vw(deck, n):
    start_time = time.time()
    success = 0
    success_through_nib = 0
    success_through_ash = 0
    at_least_1_ht = 0
    at_least_2_ht = 0
    at_least_3_ht = 0
    no_combo_hts = 0
    bar = ChargingBar('Processing', max=n/10000)
    for i in range(0, n):
        if i%10000 == 0:
            bar.next()
        test_deck = deck
        shuffle(test_deck)
        test_hand, test_deck = draw(deck, 5)
        results, nb_hts, through_nib, through_ash = vw_hand_is_combo(test_hand, test_deck, False, False)
        if results:
            success += 1
            if nb_hts >= 1:
                at_least_1_ht += 1
            if nb_hts >= 2:
                at_least_2_ht += 1
            if nb_hts >= 3:
                at_least_3_ht += 1
            if through_nib:
                success_through_nib += 1
            if through_ash:
                success_through_ash += 1
        if not results:
            no_combo_hts += nb_hts
    bar.finish()

            
    # Prints the results
    ratio_success = round(success / n * 100, 2)
    #not true
    ratio_through_nib = round(success_through_nib / n * 100, 2)
    #not true
    ratio_through_ash = round(success_through_ash / n * 100, 2)
    one_hts_ratio = round(at_least_1_ht / success * 100, 2)
    two_hts_ratio = round(at_least_2_ht / success * 100, 2)
    three_hts_ratio = round(at_least_3_ht / success * 100, 2)
    no_combo_hts_ratio = round(no_combo_hts / (n-success), 2)
    print("VW combo success Rate through no Handtraps: " + str(ratio_success) + "%")
    print("VW combo success Rate through nibiru: " + str(ratio_through_nib) + "%")
    print("VW combo success Rate through ash: " + str(ratio_through_ash) + "%")
    print("VW combo with atleast drawing 1 Handtraps in your hand: " + str(one_hts_ratio) + "%")
    print("VW combo with atleast drawing 2 Handtraps in your hand: " + str(two_hts_ratio) + "%")
    print("VW combo with atleast drawing 3 Handtraps in your hand: " + str(three_hts_ratio) + "%")
    print("Average number of Handtraps in your hand when no combo: " + str(no_combo_hts_ratio))
    print("--- %s seconds ---" % (time.time() - start_time))

def combo_pk(deck, n):
    success = 0
    success_through_nib = 0
    success_through_ash = 0
    at_least_1_ht = 0
    at_least_2_ht = 0
    at_least_3_ht = 0
    no_combo_hts = 0
    for _ in range(0, n):
        test_deck = deck
        shuffle(test_deck)
        test_hand, test_deck = draw(deck, 5)
        results, nb_hts, through_nib, through_ash = pk_hand_is_combo(test_hand, test_deck, False, False)
        if results:
            success += 1
            if nb_hts >= 1:
                at_least_1_ht += 1
            if nb_hts >= 2:
                at_least_2_ht += 1
            if nb_hts >= 3:
                at_least_3_ht += 1
        if not results:
            no_combo_hts += nb_hts
        if through_nib:
            success_through_nib += 1
        if through_ash:
            success_through_ash += 1




            
    # Prints the results
    ratio_success = round(success / n * 100, 2)
    #not true
    ratio_through_nib = round(success_through_nib / n * 100, 2)
    #not true
    ratio_through_ash = round(success_through_ash / n * 100, 2)
    one_hts_ratio = round(at_least_1_ht / success * 100, 2)
    two_hts_ratio = round(at_least_2_ht / success * 100, 2)
    three_hts_ratio = round(at_least_3_ht / success * 100, 2)
    no_combo_hts_ratio = round(no_combo_hts / (n-success), 2)
    print("PK combo success Rate through no Handtraps: " + str(ratio_success) + "%")
    print("PK combo success Rate through nibiru: " + str(ratio_through_nib) + "%")
    print("PK combo success Rate through ash: " + str(ratio_through_ash) + "%")
    print("PK combo with atleast drawing 1 Handtraps in your hand: " + str(one_hts_ratio) + "%")
    print("PK combo with atleast drawing 2 Handtraps in your hand: " + str(two_hts_ratio) + "%")
    print("PK combo with atleast drawing 3 Handtraps in your hand: " + str(three_hts_ratio) + "%")
    print("Average number of Handtraps in your hand when no combo: " + str(no_combo_hts_ratio))

