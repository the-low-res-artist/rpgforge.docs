
import re # regex operations
import sys # to return 0
import os # loop over files

# goal : to find and replace each actions with proper formatting
# example : [[Select]] ==> <span style="color:orange">Select</span>

# replace in a file
def set_highlight_actions(filename):

    # constants
    ACTION_COLOR="crimson"
    ACTION_REGEX=r"(\[\[(.+?)\]\])"

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # find all matches
    matches = re.findall(ACTION_REGEX, s)

    # safe exit
    if (len(matches) == 0):
        return

    for match in matches:
        str_to_replace=match[0]
        action=match[1]
        #str_replacement=f"<span style=\"color:{ACTION_COLOR}\">**{action}**</span>" 
        str_replacement=f"<span style=\"text-decoration: underline;\">{action}</span>"
        s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
src_root = "./../src/"
nb_files=0

for root, dirs, files in os.walk(src_root, topdown=False):
   for filename in files:
        if filename.endswith(".md"):
            set_highlight_actions(os.path.join(root, filename))
            nb_files+=1
print(f"HIGHTLIGHT ACTIONS UPDATE : {nb_files} updated")

# safe return
sys.exit(0)