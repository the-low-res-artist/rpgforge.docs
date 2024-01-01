import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files

# goal : add the custom-js link in every html output pages

# replace in a file
def set_js(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # add custom .js scripts at the end of the file
    js_link = ""
    for root, dirs, files in os.walk("./../custom-js"):
        for file in files:
            js_link += f"<script src=\"custom-js/{file}\" type=\"text/javascript\" charset=\"utf-8\"></script>"
    
    str_to_replace = "<!-- Custom JS scripts -->"
    str_replacement = f"<!-- Custom JS scripts -->{js_link}"
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)

# entry point
book_root = "./../book/"
nb_files=0

for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_js(os.path.join(root, filename))
            nb_files+=1
print(f"CUSTOM JS UPDATE : {nb_files} updated")

# safe return
sys.exit(0)