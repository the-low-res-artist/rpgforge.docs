
import re # regex operations
import sys # to return 0
import os # loop over files

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

    # Twitter / X
    str_to_replace = "DIV_HOME_BACKGROUND"
    str_replacement = "<div class=\"home-background\"></div>"
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
            basename = os.path.basename(filename)
            if (basename == "home.html" or basename == "index.html"):
                set_home(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)