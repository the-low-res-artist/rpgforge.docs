import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files
from config import config # global config

# goal : replace the favicon in each output html page

# replace in a file
def set_favicon(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # replace the favicon
    str_to_replace = '<link rel="icon" href="favicon.svg">'
    str_replacement = f"<link rel=\"icon\" href=\"{config.img_favicon}\">"
    s = s.replace(str_to_replace, str_replacement)

    str_to_replace = '<link rel="shortcut icon" href="favicon.png">'
    str_replacement = f"<link rel=\"shortcut icon\" href=\"{config.img_favicon}\">"
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)

# entry point
book_root = "./../book/"
nb_files=0
print("====================================")
print("FAVICON UPDATE")
print(f"Scanning html files in {book_root} and updating the favicon")
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_favicon(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)