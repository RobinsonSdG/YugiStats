import requests
import json
import os


filename = "D:/Documents/Code/YugiStats/Decks/Prankids/Decklists/Prankids.ydk"
target = 'D:/Documents/Code/YugiStats/Decks/Decklists/'

card_names = []
with open(filename) as f:
    lines = f.readlines()
    for line in lines[2:42]:
        response_json = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?id="+line).json()
        name = response_json['data'][0]['name']
        card_names.append(name)

textfile = open(os.path.basename(filename)+".txt", "w")
for element in card_names:
    textfile.write(element + "\n")
textfile.close()