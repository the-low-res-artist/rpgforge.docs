import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files
import time # measure duration

# goal : append a "last update" in the bottom of each page

# replace in a file
def set_last_update(filename):
    
    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # update the nav section (chapters)
    str_to_replace = "</main>"
    str_replacement = "</main><div class=\"last-update-page-container\"><div class=\"last-update-page\">Last update : Monday 20th December 2024</div></div>"
    s = s.replace(str_to_replace, str_replacement) 

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(''.join(s))

# entry point
start = time.time()
book_root = "./../book/"
nb_files=0
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_last_update(os.path.join(root, filename))
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] LAST MODIFIED UPDATE : {nb_files} updated")

# safe return
sys.exit(0)