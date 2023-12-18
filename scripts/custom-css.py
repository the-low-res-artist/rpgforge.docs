import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files

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
    for root, dirs, files in os.walk("./../custom-css"):
        for file in files:
            # special case : home.html + index.html
            if (file == "home.css"):
                basename = os.path.basename(filename)
                if (basename == "home.html" or basename == "index.html"):
                    css_link += f"<link rel=\"stylesheet\" href=\"custom-css/{file}\">"
            else:
                css_link += f"<link rel=\"stylesheet\" href=\"custom-css/{file}\">"
    str_to_replace = "<!-- Custom theme stylesheets -->"
    str_replacement = f"<!-- Custom theme stylesheets -->{css_link}"
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)

# entry point
book_root = "./../book/"
nb_files=0
print("====================================")
print("CSS UPDATE")
print(f"Scanning html files in {book_root} and adding a css link")
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_css(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)