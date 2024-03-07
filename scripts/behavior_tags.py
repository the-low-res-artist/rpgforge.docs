
import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
import time # measure duration

# goal : Update the behavior tags appearance

# replace in a file
def set_behavior_tags(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # tags container
    str_to_replace = "(<("
    str_replacement = "<p class=\"behavior_tag_container\"><p class=\"behavior_tag\">"
    s = s.replace(str_to_replace, str_replacement)

    str_to_replace = ")>)"
    str_replacement = "</div></p>"
    s = s.replace(str_to_replace, str_replacement)

    # tag
    str_to_replace = ")><("
    str_replacement = "</p><p class=\"behavior_tag\">"
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
start = time.time()
src_root = "./../book/"
nb_files=0
for root, dirs, files in os.walk(src_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_behavior_tags(os.path.join(root, filename))
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] BEHAVIOR TAGS UPDATE : {nb_files} updated")

# safe return
sys.exit(0)