
import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
import time # measure duration
import json

# goal : update the roadmap of the project

# replace in a file
def set_roadmap(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    
    # Safely read the results test filename using 'with'
    json_data = {}
    with open("./../resources/roadmap.json", 'r', encoding="utf8") as f:
        json_data = json.load(f)

    # create all versions
    versions = []
    if "versions" in json_data:
        for data in json_data["versions"]:
            index = data["index"]
            version = "<div class=\"card\"><div class=\"info\">"
            version += "<h3 class=\"title title_done\">Version " + str(index)
            version += "<div class=\"tag_container\">"
            for tag in data["tags"]:
                version += "<div class=\"tag_" + tag["color"] + "\">" + tag["text"] + "</div>"
            version += "</div></h3>"
            version += "<p> - " + "</br> - ".join(data["features"]) + "</p>"
            version += "</div></div>"
            versions.append(version)
    str_to_replace = "ROADMAP_GO_HERE"
    str_replacement = "<div class=\"timeline\">\
                           <div class=\"outer\">\
                           " + ''.join(versions) + "\
                           </div>\
                       </div>"
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
        if filename.endswith(".html"):
            basename = os.path.basename(filename)
            if (basename == "roadmap.html"):
                set_roadmap(os.path.join(root, filename))
                nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] ROADMAP UPDATE : {nb_files} updated")

# safe return
sys.exit(0)