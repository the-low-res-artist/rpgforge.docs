import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files

# goal : update the navigation summary on each html page

# replace in a file
def set_nav_summary(filename):
    
    # define regex
    CHAPTERS_SECTION_REGEX = "(<ol class=\"chapter\">.*</ol>)"
    
    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # get the chapters in the nav section
    chapters = re.findall(CHAPTERS_SECTION_REGEX, s)[0]
    chapters_new = chapters
    # safe exit
    if (len(chapters) == 0):
        return

    # hide some chapters (only used for index)
    for i in range(10):
        str_to_replace=f"<li class=\"chapter-item expanded \"><div><strong aria-hidden=\"true\">{i}.</strong> HIDE</div></li>"
        str_replacement=f"<li class=\"chapter-item hidden expanded \"><div><strong aria-hidden=\"true\">{i}.</strong> HIDE</div></li>"
        chapters_new = chapters_new.replace(str_to_replace, str_replacement)

    # update the nav section (chapters)
    str_to_replace = chapters
    str_replacement = chapters_new
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(''.join(s))

# entry point
book_root = "./../book/"
nb_files=0
print("====================================")
print("NAV SUMMARY UPDATE")
print(f"Scanning html files in {book_root} and update the navigation summary section")
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_nav_summary(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)