
from datetime import datetime # get current year
import sys # to return 0
import os # loop over files
from config import config # global config
import time # measure duration

# goal : to add a footer on each html page

# replace in a file
def set_footer(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    links=[
        {
            "href":config.link_patreon,
            "img":"footer/patreon.png",
            "alt":"Patreon link"
        },
        {
            "href":config.link_x,
            "img":"footer/x.png",
            "alt":"X/Twitter link"
        },
        {
            "href":config.link_youtube,
            "img":"footer/youtube.png",
            "alt":"Youtube link"
        },
    ]

    list_links = []
    for link in links:
        l = f"<div class=\"footer-link\">\
          <a href=\"" + link["href"] + "\" target=\"_blank\"><img src=\"https://rpgpowerforge.com/media/" + link["img"] + "\" alt=\"" + link["alt"] + "\" /></a>\
        </div>"
        list_links.append(l)
    html_links = ' '.join(list_links)

    footer=f"<p>{html_links}</p>\
    <p>Copyright © {datetime.now().year} RPG Power Forge<br>\
    \"RPG Power Forge\" is a trademark.<br>\
    Other names or brands are trademarks of their respective owners.</p>\
    <p>Last update : {datetime.now().strftime(f'%A %d %B %Y')}</p>"

    str_to_replace="</main>"
    str_replacement=f"</main><div class=\"footer-container\"><div class=\"footer-text\">{footer}</div></div>"
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
            set_footer(os.path.join(root, filename))
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] FOOTER UPDATE : {nb_files} updated")

# safe return
sys.exit(0)