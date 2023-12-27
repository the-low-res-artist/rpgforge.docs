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

    file_url=filename.replace('./../book/', 'https://rpgpowerforge.com/')

    description="The awesome documentation for the Unity package : RPG Power Forge"
    image="https://rpgpowerforge.com/media/thumbnail/thumbnail_v2.jpg"
    title="RPG Power Forge documentation site"
    author="@rpgpowerforge"
    site="rpgpowerforge.com"

    thumbnail = f"<!-- Custom HTML thumbnail image -->\
    <meta property=\"og:image\" content=\"{image}\">\
    <meta property=\"og:image:width\" content=\"1200\">\
    <meta property=\"og:image:height\" content=\"630\">\
    <meta property=\"og:image:type\" content=\"image/jpeg\">\
    <meta name=\"twitter:card\" content=\"summary_large_image\">\
    <meta name=\"twitter:site\" content=\"{author}\">\
    <meta name=\"twitter:creator\" content=\"{author}\">\
    <meta name=\"twitter:url\" content=\"{file_url}\">\
    <meta name=\"twitter:title\" content=\"{title}\">\
    <meta name=\"twitter:description\" content=\"{description}\">\
    <meta name=\"twitter:image\" content=\"{image}\">\
    <meta property=\"twitter:url\" content=\"{file_url}\">\
    <meta property=\"twitter:title\" content=\"{title}\">\
    <meta property=\"twitter:description\" content=\"{description}\">\
    <meta property=\"twitter:image\" content=\"{image}\">\
    <meta property=\"og:site_name\" content=\"{site}\">\
    <meta property=\"og:locale\" content=\"en_EN\">\
    <meta property=\"og:title\" content=\"{title}\">\
    <meta property=\"og:description\" content=\"{description}\">\
    <meta property=\"og:url\" content=\"{file_url}\">\
    <meta property=\"og:type\" content=\"article\">"
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