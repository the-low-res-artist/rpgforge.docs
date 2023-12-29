
import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
# goal : edit home to add specific div tags

# replace in a file
def set_home(filename):
    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    str_to_replace = "CARDS_GO_HERE"
    str_replacement = f"<div class=\"cards\">\
            <div class=\"card card1\" onclick=\"window.location.href = 'https://rpgpowerforge.com/en/stable/installation/introduction.html';\" style=\"cursor: pointer;\">\
                <div class=\"card-image\"><img src=\"https://rpgpowerforge.com/media/home/card_unity.png\"></img></div>\
                <div class=\"card-text\"><h3>Installation</h3><p>RPG Power Forge is your powerful Unity package to make RPG without coding. Grab the requirements and start a new project !</p></div>\
            </div>\
            <div class=\"card card2\" onclick=\"window.location.href = 'https://rpgpowerforge.com/en/stable/new_map.html';\" style=\"cursor: pointer;\">\
                <div class=\"card-image\"><img src=\"https://rpgpowerforge.com/media/home/card_getting_started.png\"></img></div>\
                <div class=\"card-text\"><h3>Getting started !</h3><p>Begin your RPG journey with all the online help you need !</p></div>\
            </div>\
            <div class=\"card card3\" onclick=\"window.location.href = '{config.link_discord}';\" style=\"cursor: pointer;\">\
                <div class=\"card-image\"><img src=\"https://rpgpowerforge.com/media/home/card_community.png\"></img></div>\
                <div class=\"card-text\"><h3>Community</h3><p>Join the dev team and users on Discord. We will listen to your feedback and try to improve our product in the right direction !</p></div>\
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
print("HOME UPDATE")
print(f"Scanning html files in {book_root} and updating home page")
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            basename = os.path.basename(filename)
            if (basename == "home.html" or basename == "index.html"):
                set_home(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)