import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files
from config import config # global config
import time # measure duration

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
    for i in range(10):
        depth = i * '../'
        str_to_replace = f"href=\"{depth}favicon.svg\">"
        str_replacement = f"href=\"{config.img_favicon}\">"
        s = s.replace(str_to_replace, str_replacement)

        str_to_replace = f"href=\"{depth}favicon.png\">"
        str_replacement = f"href=\"{config.img_favicon}\">"
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
            set_favicon(os.path.join(root, filename))
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] FAVICON UPDATE : {nb_files} updated")

# safe return
sys.exit(0)