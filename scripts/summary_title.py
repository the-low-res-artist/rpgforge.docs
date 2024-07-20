
import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
import time # measure duration

# goal : Add a title section to the summary

# replace in a file
def set_summary_title(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    str_to_replace = "<ol class=\"chapter\">"
    str_replacement = f"\
    <div class=\"summary-title-container\">\
      <img src=\"https://rpgpowerforge.com/media/logo/nav-logo.jpg\" alt=\"product logo\" class=\"nav-logo\">\
      <div class=\"summary-title\">{config.doc_website_title}</div>\
      <div class=\"summary-subtitle\">{config.doc_website_subtitle}</div>\
    </div>\
    <ol class=\"chapter\">"
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
            set_summary_title(os.path.join(root, filename))
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] SUMMARY TITLE UPDATE : {nb_files} updated")

# safe return
sys.exit(0)