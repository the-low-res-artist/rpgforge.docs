
import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
import time # measure duration

# goal : edit the external links

# replace in a file
def set_link_md(filename):
    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return
    

    # Patreon
    str_to_replace = "(link_patreon)"
    str_replacement = f"({config.link_patreon})"
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)

# entry point
start = time.time()
book_root = "./../src/"
nb_files=0

for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".md"):
            set_link_md(os.path.join(root, filename))
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] LINKS MARKDOWN UPDATE : {nb_files} updated")

# safe return
sys.exit(0)