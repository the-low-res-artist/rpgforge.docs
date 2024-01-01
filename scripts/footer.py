
from datetime import datetime # get current year
import sys # to return 0
import os # loop over files
from config import config # global config

# goal : to add a footer on each html page

# replace in a file
def set_footer(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    discord_link=f"<div class=\"footer-link\"><a href=\"{config.link_discord}\" target=\"_blank\"><img src=\"https://rpgpowerforge.com/media/footer/discord.png\" alt=\"Discord logo\" /></a></div>"
    x_link=f"<div class=\"footer-link\"><a href=\"{config.link_x}\" target=\"_blank\"><img src=\"https://rpgpowerforge.com/media/footer/x.png\" alt=\"X/Twitter logo\" /></a></div>"
    trello_link=f"<div class=\"footer-link\"><a href=\"{config.link_trello}\" target=\"_blank\"><img src=\"https://rpgpowerforge.com/media/footer/trello.png\" alt=\"Trello logo\" /></a></div>"

    footer=f"<p>{discord_link} {x_link} {trello_link}</p>\
    <p>Copyright © {datetime.now().year} RPG Power Forge</p>\
    <p>\"RPG Power Forge\" is a trademark.</p>\
    <p>Other names or brands are trademarks of their respective owners.</p>"

    str_to_replace="<nav class=\"nav-wide-wrapper\" aria-label=\"Page navigation\">"
    str_replacement=f"<div class=\"footer-container\"><div class=\"footer-text\">{footer}</div></div><nav class=\"nav-wide-wrapper\" aria-label=\"Page navigation\">"
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
src_root = "./../book/"
nb_files=0
print("====================================")
print("FOOTER UPDATE")
print(f"Scanning html files in {src_root} and add a footer part")
for root, dirs, files in os.walk(src_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_footer(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)