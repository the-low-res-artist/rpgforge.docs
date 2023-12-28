
from datetime import datetime # get current year
import sys # to return 0
import os # loop over files

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

    discord_link="<div class=\"footer-link\"><a href=\"https://x.com\" target=\"_blank\"><img src=\"https://rpgpowerforge.com/media/footer/discord.png\" /></a></div>"
    x_link="<div class=\"footer-link\"><a href=\"https://x.com\" target=\"_blank\"><img src=\"https://rpgpowerforge.com/media/footer/x.png\" /></a></div>"
    trello_link="<div class=\"footer-link\"><a href=\"https://trello.com/b/PIzgsYov/rpg-power-forge-road-map\" target=\"_blank\"><img src=\"https://rpgpowerforge.com/media/footer/trello.png\" /></a></div>"

    footer=f"<p>{discord_link}{x_link}{trello_link}</p>\
    <p>Copyright © {datetime.now().year} RPG Power Forge</p>\
    <p>\"RPG Power Forge\", RPG Power Forge logos, and other RPG Power Forge trademarks are trademarks or registered trademarks.</p>\
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