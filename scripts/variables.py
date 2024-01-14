
import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
import time # measure duration

# goal : replace variables in md files with their values

# replace in a file
def set_variables(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    for key, value in config.md_variables.items():
        str_to_replace = key
        str_replacement = value
        s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
start = time.time()
src_root = "./../src/"
nb_files=0
for root, dirs, files in os.walk(src_root, topdown=False):
   for filename in files:
        if filename.endswith(".md"):
            set_variables(os.path.join(root, filename))
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] VARIABLES UPDATE : {nb_files} updated")

# safe return
sys.exit(0)