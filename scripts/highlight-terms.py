
import re # regex operations
import sys # to return 0
import os # loop over files

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

    terms = [
        'Unity',
        'Hub',
        'RPG Power Forge',
        'Editor'
    ]

    for term in terms:
        str_to_replace=term
        str_replacement=f"**{term}**"
        s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
src_root = "./../src/"
nb_files=0
print("====================================")
print("HIGHLIGHT TERMS UPDATE")
print(f"Scanning md files in {src_root} and formatting key terms")
for root, dirs, files in os.walk(src_root, topdown=False):
   for filename in files:
        if filename.endswith(".md"):
            set_highlight_terms(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)