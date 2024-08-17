
import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
import time # measure duration

# goal : ???

# replace in a file
def set_devlogs(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    str_to_replace = "DEVLOGS_GO_HERE"
    str_replacement = ""

    devlog_id = 1
    for dev in config.devlogs:
        title = dev["title"]
        iframe = dev["iframe"]
        devlog_str = f"<h3>Devlog #{devlog_id} : {title}</h3>\n{iframe}\n"       
        str_replacement = f"{str_replacement}\n{devlog_str}"
        devlog_id += 1

    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
start = time.time()
src_root = "./../book/"
nb_files=0
for root, dirs, files in os.walk(src_root, topdown=False):
   for filename in files:
        if filename.endswith("devlogs.html"):
            set_devlogs(os.path.join(root, filename))
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] DEVLOGS UPDATE : {nb_files} updated")

# safe return
sys.exit(0)