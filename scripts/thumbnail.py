import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files
from PIL import ImageFont, ImageDraw, Image

# goal : add a nice thumbnail to html output pages

# add a cool title to the thumbnail
def get_new_thumbnail_image(filename, title, file_template):
    basename = os.path.basename(filename)
    
    # open template image
    with Image.open(file_template) as image:

        # get the image
        draw = ImageDraw.Draw(image)

        # text to draw
        subtitle = "User manual"

        # create 2 fonts
        font_title = ImageFont.truetype("./../font/mont.otf", 110)
        font_subtitle = ImageFont.truetype("./../font/mont.otf", 50)
        front_color = (255, 255, 255, 255)
        back_color = (0, 0, 0, 255)

        # title
        for x in range(-4,5,2):
            for y in range(-4, 5, 2):
                draw.text((20+x, 400+y), title, font=font_title, fill=back_color)
        draw.text((20, 400), title, font=font_title, fill=front_color)

        # subtitle
        for x in range(-4,5,2):
            for y in range(-4, 5, 2):
                draw.text((23+x, 500+y), subtitle, font=font_subtitle, fill=back_color)
        draw.text((23, 500), subtitle, font=font_subtitle, fill=front_color)

        # save
        output_filename = title.replace(" ","_").lower()
        thumbnail_path = f"./../media/thumbnail/thumbnail_{output_filename}.jpg"
        image.save(thumbnail_path)

    return thumbnail_path.replace("./../", "https://rpgpowerforge.com/")

# replace in a file
def set_thumbnail(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # get file title
    title = s[0]

    file_url=filename.replace('./../book/', 'https://rpgpowerforge.com/')
    description="The awesome documentation for the Unity package : RPG Power Forge"
    image= get_new_thumbnail_image(filename, title, "./../media/thumbnail/thumbnail_template.png")
    title="RPG Power Forge documentation site"
    author="@rpgpowerforge"
    site="rpgpowerforge.com"

    thumbnail = f"<!-- Custom HTML thumbnail image and metadata -->\
    <meta property=\"og:image\" content=\"{image}\">\
    <meta property=\"og:image:width\" content=\"1200\">\
    <meta property=\"og:image:height\" content=\"630\">\
    <meta property=\"og:image:type\" content=\"image/jpeg\">\
    \
    <meta property=\"og:site_name\" content=\"{site}\">\
    <meta property=\"og:locale\" content=\"en_EN\">\
    <meta property=\"og:title\" content=\"{title}\">\
    <meta property=\"og:description\" content=\"{description}\">\
    <meta property=\"og:url\" content=\"{file_url}\">\
    <meta property=\"og:type\" content=\"article\">\
    \
    <meta property=\"og:rating\" content=\"1\">\
    <meta property=\"og:rating_scale\" content=\"2\">\
    <meta property=\"og:rating_count\" content=\"3\">\
    \
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
    <meta property=\"twitter:image\" content=\"{image}\">"

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