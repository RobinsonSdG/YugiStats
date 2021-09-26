from combo_simulator import combo_vw, combo_pk


def import_deck(filename):
    with open(filename) as f:
        deck = [line.strip() for line in f if not line.startswith('#')]
        return deck


# What decklist we want to import and how many hands we want to simulate
def main(deck_txt, n):
    print(deck_txt)
    deck = import_deck(deck_txt)
    combo_vw(deck, n)
    #combo_pk(deck, n)

# Using 25000 so it runs quicker as this is an online IDE
#main("D:\Documents\Code\YugiStats\Decks\Virtual_World\Decklists\Virtual_World_3Pr_2De.txt", 100000)
main("D:\Documents\Code\YugiStats\Decks\Virtual_World\Decklists\Virtual_World_Rob.txt", 100000)
#main("D:\Documents\Code\YugiStats\Decks\Virtual_World\Decklists\Virtual_World.test.txt", 100000)
#main("D:\Documents\Code\YugiStats\Decks\Prankids\Decklists\Prankids.ydk.txt", 100000)


