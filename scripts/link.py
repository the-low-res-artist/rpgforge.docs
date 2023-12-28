
import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
# goal : edit the external links

# replace in a file
def set_link(filename):
    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return
    
    # I add 'target=\"_blank\"' to make the click open a new tab

    # Discord
    str_to_replace = "<div><strong aria-hidden=\"true\">4.1.</strong> link_discord</div>"
    str_replacement = f"<a href=\"{config.link_discord}\" target=\"_blank\"><strong aria-hidden=\"true\">4.1.</strong> Discord server</a>"
    str_replacement = "<a href=\"https://trello.com/b/PIzgsYov/rpg-power-forge-road-map\" target=\"_blank\""
    s = s.replace(str_to_replace, str_replacement)

    # Twitter / X
    str_to_replace = "<div><strong aria-hidden=\"true\">4.2.</strong> link_x</div><"
    str_replacement = f"<a href=\"{config.link_x}\" target=\"_blank\"><strong aria-hidden=\"true\">4.2.</strong> Twitter / X</a>"
    s = s.replace(str_to_replace, str_replacement)

    # Trello
    str_to_replace = "<div><strong aria-hidden=\"true\">4.3.</strong> link_trello</div>"
    str_replacement = f"<a href=\"{config.link_trello}\" target=\"_blank\"><strong aria-hidden=\"true\">4.3.</strong> Trello</a>"
    s = s.replace(str_to_replace, str_replacement)


    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
book_root = "./../book/"
nb_files=0
print("====================================")
print("LINKS UPDATE")
print(f"Scanning html files in {book_root} and adding external links in nav summary")
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_link(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)