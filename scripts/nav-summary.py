import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files
import time # measure duration

# goal : update the navigation summary on each html page

# replace in a file
def set_nav_summary(filename):
    
    # define regex
    NUMBER_CHAPTER_REGEX = "(<strong aria-hidden=\"true\">([0-9]+\.)+</strong>)"
    
    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # get the chapters in the nav section
    number_chapters = re.findall(NUMBER_CHAPTER_REGEX, s)
    # safe exit
    if (len(number_chapters) == 0):
        return

    # remove numbers in chapter title
    for number in number_chapters:
        str_to_replace = number
        str_replacement = ""
        s = s.replace(str_to_replace, str_replacement) 

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(''.join(s))

# entry point
start = time.time()
book_root = "./../book/"
nb_files=0
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_nav_summary(os.path.join(root, filename))
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] NAV SUMMARY UPDATE : {nb_files} updated")

# safe return
sys.exit(0)