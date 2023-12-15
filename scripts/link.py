
import re # regex operations
import sys # to return 0
import os # loop over files

# goal : edit the external links by removing ".html" at the end

# replace in a file
def set_link(filename):
    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # Twitter / X
    str_to_replace = "<a href=\"../https://twitter.com/RPGPowerForge.html\""
    str_replacement = "<a href=\"https://twitter.com/RPGPowerForge\" target=\"_blank\""
    s = s.replace(str_to_replace, str_replacement)

    str_to_replace = "<a href=\"../https://x.com/RPGPowerForge.html\""
    str_replacement = "<a href=\"https://x.com/RPGPowerForge\" target=\"_blank\""
    s = s.replace(str_to_replace, str_replacement)

    # Trello
    str_to_replace = "<a href=\"../https://trello.com/b/PIzgsYov/rpg-power-forge-road-map.html\""
    str_replacement = "<a href=\"https://trello.com/b/PIzgsYov/rpg-power-forge-road-map\" target=\"_blank\""
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
book_root = "./../book/"
nb_files=0
print("====================================")
print("LINKS UPDATE")
print(f"Scanning html files in {book_root} and fixing external links suffixes")
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_link(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)