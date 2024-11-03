import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files
import time # measure duration

# goal : add an html dropdown menu on each page to select the doc language

# helper
def get_glag(lang):
    if lang == "doc": return 🇫🇷
    return ""

# replace in a file
def set_language(filename, lang_list):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # build language selection
    # button class
    objects_html =  "<button id=\"language-toggle\" class=\"icon-button\" type=\"button\" title=\"Change language\" aria-label=\"Change language\""
    objects_html += "aria-haspopup=\"true\" aria-expanded=\"false\" aria-controls=\"language-list\">"
    objects_html += "<i class=\"fa fa-globe\"></i></button>"
    # dropdown class
    objects_html += "<ul id=\"language-list\" class=\"theme-popup\" aria-label=\"languages\" role=\"menu\" style=\"display: none;\">"
    # dropdown items
    for lang in lang_list:
        flag = get_flag(lang)
        objects_html += f"<li role=\"none\"><button role=\"menuitem\" class=\"theme\" id=\"{lang}\">{flag} {lang}</button></li>"
    objects_html += "</ul>"

    str_to_replace = "<div class=\"left-buttons\">"
    str_replacement = str_to_replace + objects_html
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)

# entry point
start = time.time()

src_root = "./../src/"
lang_list=""
for root, dirs, files in os.walk(src_root, topdown=False):
    if root == src_root:
        lang_list = dirs
book_root = "./../book/"
nb_files=0
for root, dirs, files in os.walk(book_root, topdown=False):
    current_lang=""
    for filename in files:
        # get current language
        if filename.endswith(".html"):
            set_language(os.path.join(root, filename), lang_list)
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] LANGAGE UPDATE : {nb_files} updated")

# safe return
sys.exit(0)