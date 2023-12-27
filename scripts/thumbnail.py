import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files

# goal : add a nice thumbnail to html output pages

# replace in a file
def set_thumbnail(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    thumbnail = "<!-- Custom HTML thumbnail image -->\
    <meta property=\"og:image\" content=\"https://rpgpowerforge.com/media/thumbnail/thumbnail_v2.jpg\">\
    <meta property=\"og:image:width\" content=\"1200\">\
    <meta property=\"og:image:height\" content=\"630\">"

    str_to_replace = "</head>"
    str_replacement = f"{thumbnail}</head>"
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)

# entry point
book_root = "./../book/"
nb_files=0
print("====================================")
print("THUMBNAILS UPDATE")
print(f"Scanning html files in {book_root} and adding a link thumbnail")
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_thumbnail(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)