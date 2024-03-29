
import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
import time # measure duration

# goal : to find and replace each important term formatting
# example : Unity ==> **Unity**

# replace in a file
def set_highlight_terms(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    for term in config.highlight_terms:
        pattern=term
        str_replacement=f"**{term}**"
        s = re.sub('pattern', str_replacement, s)
        #s = s.replace(str_to_replace, str_replacement)

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
            set_highlight_terms(os.path.join(root, filename))
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] HIGHLIGHT TERMS UPDATE : {nb_files} updated")

# safe return
sys.exit(0)