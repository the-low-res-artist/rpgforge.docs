import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files
import time # measure duration
from config import config

# goal : add the custom-css link in every html output pages

# replace in a file
def set_css(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # add custom .css scripts at the end of the file
    css_link = ""
    basename = os.path.basename(filename)

    common_list = config.css_common_list
    black_list = config.css_black_list

    for root, dirs, files in os.walk("./../custom-css"):
        for file in files:
            # skip black list css files
            if file in black_list:
                continue
            # add if in common list
            if file in common_list:
                css_link += f"<link rel=\"stylesheet\" href=\"custom-css/{file}\">"
            # also add if css file same name as html file
            else:
                html_filename = basename.split('.')[0]
                # index and home are the same page
                if html_filename == "index":
                    html_filename = "home"
                css_filename =  file.split('.')[0]
                if html_filename == css_filename:
                    css_link += f"<link rel=\"stylesheet\" href=\"custom-css/{file}\">"
    str_to_replace = "<!-- Custom theme stylesheets -->"
    str_replacement = f"<!-- Custom theme stylesheets -->{css_link}"
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
            set_css(os.path.join(root, filename))
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] CUSTOM CSS UPDATE : {nb_files} updated")

# safe return
sys.exit(0)