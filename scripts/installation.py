import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
import random
import time # measure duration

# goal : edit dev team page to add specific div tags

# replace in a file
def set_installation(filename):
    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # prepare funny tags
    tags_install_unity = ""
    for tag in config.tags_install_unity:
        tags_install_unity += f"<div class=\"tag\" style=\"background-color:SlateBlue\">{tag}</div>"
    tags_install_unity = f"<div class=\"tags_container\">{tags_install_unity}</div>"

    tags_dl_rpgpowerforge = ""
    for tag in config.tags_dl_rpgpowerforge:
        tags_dl_rpgpowerforge += f"<div class=\"tag\" style=\"background-color:RoyalBlue\">{tag}</div>"
    tags_dl_rpgpowerforge = f"<div class=\"tags_container\">{tags_dl_rpgpowerforge}</div>"

    tags_create_project = ""
    for tag in config.tags_create_project:
        tags_create_project += f"<div class=\"tag\" style=\"background-color:DodgerBlue\">{tag}</div>"
    tags_create_project = f"<div class=\"tags_container\">{tags_create_project}</div>"

    # setup cards
    str_to_replace = "CARDS_GO_HERE"
    str_replacement = f"<div class=\"cards\">\
            <div class=\"card card1\" onclick=\"window.location.href = 'https://rpgpowerforge.com/en/stable/installation/installation_unity.html';\" style=\"cursor: pointer;\">\
                <div class=\"card-image\"><img src=\"https://rpgpowerforge.com/media/installation/card_unity.png\"></img></div>\
                <div class=\"card-text\"><h3>{config.title_install_unity}</h3>{tags_install_unity}<p>{config.description_install_unity}</p></div>\
            </div>\
            <div class=\"card card2\" onclick=\"window.location.href = 'https://rpgpowerforge.com/en/stable/installation/download_rpg_power_forge.html';\" style=\"cursor: pointer;\">\
                <div class=\"card-image\"><img src=\"https://rpgpowerforge.com/media/installation/card_rpf.png\"></img></div>\
                <div class=\"card-text\"><h3>{config.title_dl_rpgpowerforge}</h3>{tags_dl_rpgpowerforge}<p>{config.description_dl_rpgpowerforge}</p></div>\
            </div>\
            <div class=\"card card3\" onclick=\"window.location.href = 'https://rpgpowerforge.com/en/stable/installation/create_new_project.html';\" style=\"cursor: pointer;\">\
                <div class=\"card-image\"><img src=\"https://rpgpowerforge.com/media/installation/card_new_project.png\"></img></div>\
                <div class=\"card-text\"><h3>{config.title_create_project}</h3>{tags_create_project}<p>{config.description_create_project}</p></div>\
            </div>\
        </div>"

    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
start = time.time()
book_root = "./../book/"
nb_files=0

for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            basename = os.path.basename(filename)
            if (basename == "installation.html"):
                set_installation(os.path.join(root, filename))
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] INSTALLATION UPDATE : {nb_files} updated")

# safe return
sys.exit(0)