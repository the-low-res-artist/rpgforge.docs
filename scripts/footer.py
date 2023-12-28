
import re # regex operations
import sys # to return 0
import os # loop over files

# goal : to add a footer on each html page

# replace in a file
def set_footer(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    str_to_replace="<nav class=\"nav-wide-wrapper\" aria-label=\"Page navigation\">"
    str_replacement=f"<div class=\"website-footer\">footer part</div><nav class=\"nav-wide-wrapper\" aria-label=\"Page navigation\">"
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
src_root = "./../src/"
nb_files=0
print("====================================")
print("FOOTER UPDATE")
print(f"Scanning md files in {src_root} and add a footer part")
for root, dirs, files in os.walk(src_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_footer(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)