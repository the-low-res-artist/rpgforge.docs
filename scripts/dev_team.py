
import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
# goal : edit dev team page to add specific div tags

# replace in a file
def set_dev_team(filename):
    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    str_to_replace = "CARDS_GO_HERE"
    str_replacement = f"<div class=\"cards\">\
            <div class=\"card card1\">\
                <div class=\"card-image\"><img src=\"https://rpgpowerforge.com/media/dev_team/card_gif.png\"></img></div>\
                <div class=\"card-text\"><h3>Gif</h3><p>description goes here</p></div>\
            </div>\
            <div class=\"card card2\">\
                <div class=\"card-image\"><img src=\"https://rpgpowerforge.com/media/dev_team/card_chiw.png\"></img></div>\
                <div class=\"card-text\"><h3>Chiw</h3><p>description goes here</p></div>\
            </div>\
            <div class=\"card card3\">\
                <div class=\"card-image\"><img src=\"https://rpgpowerforge.com/media/dev_team/card_noiracide.png\"></img></div>\
                <div class=\"card-text\"><h3>Noiracide</h3><p>description goes here</p></div>\
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
print("DEV TEAM UPDATE")
print(f"Scanning html files in {book_root} and updating dev team page")
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            basename = os.path.basename(filename)
            if (basename == "dev_team.html"):
                set_dev_team(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)