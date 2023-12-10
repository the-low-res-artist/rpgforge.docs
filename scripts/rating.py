import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files

# goal : add a rating at the bottom of each page

# replace in a file
def set_rating(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    current_rate_htlm="<div style=\"font-size:13px;font-weight: normal;opacity: 0.5;\"><i>Users find this page helpful</i></div>"

    # add the subtitle on top of the page
    str_to_replace = "</a></h1>"
    str_replacement = f"</a>{current_rate_htlm}</h1>"
    s = s.replace(str_to_replace, str_replacement)
    

    with open("./../resources/rating.html") as f:
        rating_html = f.read()

    # add custom .css scripts at the end of the file
    str_to_replace = "</main>"
    str_replacement = f"{rating_html}</main>"
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)

# entry point
book_root = "./../book/"
nb_files=0
print("====================================")
print("RATE UPDATE")
print(f"Scanning html files in {book_root} and adding a rating option")
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_rating(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)