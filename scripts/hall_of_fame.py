
import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
import time # measure duration

# goal : ???

# replace in a file
def set_hall_of_fame(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    str_to_replace = "SUPPORTER_LIST_GOES_HERE"
    str_replacement = ""

    supporters = sorted(config.supporters, key=lambda d: d['name'])

    for sup in supporters:
        name = sup["name"]
        sub_str = f"* **{name}**"
        if "link" in sup:
            link = sup["link"]
            link_text = link.replace("http://", "")
            link_text = link.replace("https://", "")
            sub_str = f"{sub_str} : [{link_text}]({link})"
        str_replacement = f"{str_replacement}\n{sub_str}"

    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
start = time.time()
src_root = "./../src/"
nb_files=0
for root, dirs, files in os.walk(src_root, topdown=False):
   for filename in files:
        if filename.endswith("hall_of_fame.md"):
            set_hall_of_fame(os.path.join(root, filename))
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] HALL OF FAME UPDATE : {nb_files} updated")

# safe return
sys.exit(0)