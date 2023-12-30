import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
import random

# goal : edit lets make a game page to add specific div tags

# replace in a file
def set_lets_make_a_game(filename):
    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # prepare funny tags
    tags_2d = ""
    for tag in config.tags_2d:
        tags_2d += f"<div class=\"tag\" style=\"background-color:ForestGreen\">{tag}</div>"
    tags_2d = f"<div class=\"tags_container\">{tags_2d}</div>"

    tags_3d = ""
    for tag in config.tags_3d:
        tags_3d += f"<div class=\"tag\" style=\"background-color:Chocolate\">{tag}</div>"
    tags_3d = f"<div class=\"tags_container\">{tags_3d}</div>"

    tags_4d = ""
    for tag in config.tags_4d:
        tags_4d += f"<div class=\"tag\" style=\"background-color:Crimson\">{tag}</div>"
    tags_4d = f"<div class=\"tags_container\">{tags_4d}</div>"

    # setup cards
    str_to_replace = "CARDS_GO_HERE"
    str_replacement = f"<div class=\"cards\">\
            <div class=\"card card1\" onclick=\"window.location.href = 'https://cursoreffects.com/';\" style=\"cursor: pointer;\">\
                <div class=\"card-image\"><img src=\"https://rpgpowerforge.com/media/lets_make_a_game/card_2d.png\"></img></div>\
                <div class=\"card-text\"><h3>{config.title_2d}</h3>{tags_2d}<p>{config.description_2d}</p></div>\
            </div>\
            <div class=\"card card2\" onclick=\"window.location.href = 'https://jacksonpollock.org/';\" style=\"cursor: pointer;\">\
                <div class=\"card-image\"><img src=\"https://rpgpowerforge.com/media/lets_make_a_game/card_3d.png\"></img></div>\
                <div class=\"card-text\"><h3>{config.title_3d}</h3>{tags_3d}<p>{config.description_3d}</p></div>\
            </div>\
            <div class=\"card card3\" onclick=\"window.location.href = 'https://burymewithmymoney.com/';\" style=\"cursor: pointer;\">\
                <div class=\"card-image\"><img src=\"https://rpgpowerforge.com/media/lets_make_a_game/card_4d.png\"></img></div>\
                <div class=\"card-text\"><h3>{config.title_4d}</h3>{tags_4d}<p>{config.description_4d}</p></div>\
            </div>\
        </div>"

    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
book_root = "./../book/"
nb_files=0
print("====================================")
print("LETS MAKE A GAME UPDATE")
print(f"Scanning html files in {book_root} and updating the lets make a game page")
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            basename = os.path.basename(filename)
            if (basename == "lets_make_a_game.html"):
                set_lets_make_a_game(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)