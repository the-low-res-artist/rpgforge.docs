
import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
import time # measure duration

# goal : update the features

# replace in a file
def set_features(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # Safely read the results test filename using 'with'
    json_data = {}
    with open("./../resources/features.json", 'r', encoding="utf8") as f:
        json_data = json.load(f)

    # create all features
    sections = []
    if "sections" in json_data:
        for section in json_data["sections"]:
                     
            title = section["title"]
            description = section["description"]
            
            section_html = f"<h3>{title}</h3>" 
            section_html += f"<div class=\"feature_description\">{description}</div>" 

            # features
            features = ""
            for feature in section["features"]:
                name = feature["name"]
                state = feature["state"]
                color = "gray"
                
                if "color" in feature:
                    color = section["color"]

                features_html += f"<div class=\"feature_container\">\
                        <div class=\"feature_name\">{name}</div>\
                        <div class=\"tag_{color}\">{state}</div>\
                    </div>"

            section_html += f"<div class=\"features_container\">{feature_html}</div>"
            sections.append(section_html)

    str_to_replace = "<p>FEATURES_GO_HERE</p>"
    str_replacement = ''.join(sections) 
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
            if (basename == "features.html"):
                set_features(os.path.join(root, filename))
                nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] FEATURES UPDATE : {nb_files} updated")

# safe return
sys.exit(0)