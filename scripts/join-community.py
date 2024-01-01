import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files
from config import config
# goal : update the top bar and add a button

# replace in a file
def set_join_community(filename):
    
    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # update the top bar section
    str_to_replace = "<h1 class=\"menu-title\">RPG Power Forge</h1>"
    str_replacement = f"<h1 class=\"menu-title\">RPG Power Forge</h1><div class=\"join-community-container\"><div class=\"join-community-text\"><a href=\"{config.link_discord}\" target=\"_blank\">Join us soon !</a></div></div>"
    s = s.replace(str_to_replace, str_replacement) 

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(''.join(s))

# entry point
book_root = "./../book/"
nb_files=0
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_join_community(os.path.join(root, filename))
            nb_files+=1
print(f"JOIN COMMUNITY UPDATE : {nb_files} updated")

# safe return
sys.exit(0)