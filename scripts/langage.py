import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files

# goal : add an html dropdown menu on each page to select the doc langage

# replace in a file
def set_langage(filename):

    TOP_BUTTON_REGEX = r"(<div class=\"left-buttons\">)"

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # find all matches
    matches = re.findall(TOP_BUTTON_REGEX, s)

    # safe exit
    if (len(matches) == 0):
        return

    # build langage selection
    langage_list = ["English", "Français", "中文", "日本語"]
    # button class
    objects_html =  "<button id=\"langage-toggle\" class=\"icon-button\" type=\"button\" title=\"Change langage\" aria-label=\"Change langage\""
    objects_html += "aria-haspopup=\"true\" aria-expanded=\"false\" aria-controls=\"langage-list\">"
    objects_html += "<i class=\"fa fa-globe\"></i>"
    objects_html += "Langages</button>"
    # dropdown class
    objects_html += "<ul id=\"langage-list\" class=\"theme-popup\" aria-label=\"langages\" role=\"menu\" style=\"display: none;\">"
    # dropdown items
    for langage in langage_list:
        objects_html += f"<li role=\"none\"><button role=\"menuitem\" class=\"theme\" id=\"{langage}\">{langage}</button></li>"
    objects_html += "</ul>"

    for match in matches:
        str_to_replace = match
        str_replacement = match + objects_html
        s = s.replace(str_to_replace, str_replacement)

    # add custom .js scripts at the end of the file
    str_to_replace = "<!-- Custom JS scripts -->"
    str_replacement = "<!-- Custom JS scripts --><script src=\"js/langage.js\" type=\"text/javascript\" charset=\"utf-8\"></script>"
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)

# entry point
root = "./../book/"
nb_files=0
print("====================================")
print("LANGAGE UPDATE")
print(f"Scanning html files in {root} and adding a Langage dropdown")
for root, dirs, files in os.walk(root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_langage(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)