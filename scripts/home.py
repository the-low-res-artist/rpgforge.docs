
import re # regex operations
import sys # to return 0
import os # loop over files

# goal : edit home to add specific div tags

# replace in a file
def set_home(filename):
    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # home
    heros_text = "The Maker of RPG"
    community_link= "<a href=\"https://rpgpowerforge.com/\"><img src=\"./../../../media/home/join_discord.png\" alt=\"join_discord.png\"></a>"
    value_1 = ["100", "value text 1"]
    value_2 = ["200", "value text 2"]
    value_3 = ["300", "value text 3"]

    str_to_replace = "DIV_HOME"
    str_replacement = f"<div class=\"home-background\"></div>\
    <div class=\"home-text\">{heros_text}</div>\
    <div class=\"home-community\">{community_link}</div>\
    <div class=\"home-values\">\
        <div class=\"home-value\">\
            <div class=\"home-value-number\">{value_1[0]}</div>\
            <div class=\"home-value-text\">{value_1[1]}</div>\
        </div>\
        <div class=\"home-value\">\
            <div class=\"home-value-number\">{value_2[0]}</div>\
            <div class=\"home-value-text\">{value_2[1]}</div>\
        </div>\
        <div class=\"home-value\">\
            <div class=\"home-value-number\">{value_3[0]}</div>\
            <div class=\"home-value-text\">{value_3[1]}</div>\
        </div>\
    </div>"
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
book_root = "./../book/"
nb_files=0
print("====================================")
print("LINKS UPDATE")
print(f"Scanning html files in {book_root} and fixing external links suffixes")
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            basename = os.path.basename(filename)
            if (basename == "home.html" or basename == "index.html"):
                set_home(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)