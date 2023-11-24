import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files

# goal : add an html dropdown menu on each page to select the doc version

# replace in a file
def set_version(filename, version_list, current_version):

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

    # build version selection
    # button class
    objects_html =  "<button id=\"version-toggle\" class=\"icon-button\" type=\"button\" title=\"Change version\" aria-label=\"Change version\""
    objects_html += "aria-haspopup=\"true\" aria-expanded=\"false\" aria-controls=\"version-list\">"
    objects_html += "<i class=\"fa fa-code-fork\"></i>"
    objects_html += f"{current_version}</button>"
    # dropdown class
    objects_html += "<ul id=\"version-list\" class=\"theme-popup\" aria-label=\"Versions\" role=\"menu\" style=\"display: none;\">"
    # dropdown items
    for version in version_list:
        objects_html += f"<li role=\"none\"><button role=\"menuitem\" class=\"theme\" id=\"{version}\">{version}</button></li>"
    objects_html += "</ul>"

    for match in matches:
        str_to_replace = match
        str_replacement = match + objects_html
        s = s.replace(str_to_replace, str_replacement)

    # add custom .js scripts at the end of the file
    str_to_replace = "<!-- Custom JS scripts -->"
    str_replacement = "<!-- Custom JS scripts --><script src=\"js/version.js\" type=\"text/javascript\" charset=\"utf-8\"></script>"
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)

# entry point
book_root = "./../src/"
nb_files=0
print("====================================")
print("VERSION UPDATE")
print(f"Scanning html files in {book_root} and adding a Version dropdown")
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        # get current language
        current_lang=root.replace(book_root,'').split('\\')[0].split('/')[0]
        # get current version
        current_version=root.replace(book_root,'')[3:].split('\\')[0].split('/')[0]
        # get version list
        potential_versions= os.listdir(os.path.join(book_root, current_lang))
        version_list = []
        for version in potential_versions: # loop through all the files and folders (no recursive)
            if os.path.isdir(os.path.join(book_root, current_lang, filename)): # check whether the current object is a folder or not
                version_list.append(version)
        if filename.endswith(".html"):
            set_version(os.path.join(root, filename), version_list, current_version)
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)