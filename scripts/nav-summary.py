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

    # reformat some chapters
    # Home
    #str_to_replace="<li class=\"chapter-item expanded affix \"><a href=\"front_page.html\">Home</a></li>"
    #str_replacement="<li class=\"part-title expanded affix\"><a href=\"front_page.html\">Home <i class=\"fa fa-home\"></i></a></li>"
    #chapters_new = chapters_new.replace(str_to_replace, str_replacement)
    
    #str_to_replace="<div class=\"sidebar-scrollbox\"><ol class=\"chapter\"><li class=\"chapter-item expanded affix \">"
    #str_replacement="<div class=\"sidebar-scrollbox\"><ol class=\"chapter\"><li class=\"part-title expanded affix \">"
    #chapters_new = chapters_new.replace(str_to_replace, str_replacement)
    
    # 1. Installation
    expand = "expanded"
    str_to_replace="<li class=\"chapter-item expanded \"><div><strong aria-hidden=\"true\">1.</strong> Installation</div></li>"
    str_replacement=f"<li class=\"part-title {expand} \" id=\"li-installation\"><button class=\"button-summary\" id=\"button-installation\" title=\"Installation\"><strong aria-hidden=\"true\"><i class=\"fa fa-chevron-down\" id=\"chevron-installation\"></i>&nbsp;&nbsp;Installation&nbsp;&nbsp;<i class=\"fa fa-download\"></i></strong></button></li>"
    chapters_new = chapters_new.replace(str_to_replace, str_replacement)
    
    # 2. Getting started
    expand = ""
    if ("/getting_started/" in filename):
        expand = "expanded"
    str_to_replace="<li class=\"chapter-item expanded \"><div><strong aria-hidden=\"true\">2.</strong> Getting started</div></li>"
    str_replacement=f"<li class=\"part-title {expand} \" id=\"li-getting-started\"><button class=\"button-summary\" id=\"button-getting-started\" title=\"Getting Started\"><strong aria-hidden=\"true\"><i class=\"fa fa-chevron-right\" id=\"chevron-getting-started\"></i>&nbsp;&nbsp;Getting started&nbsp;&nbsp;<i class=\"fa fa-bolt\"></i></strong></button></li>"
    chapters_new = chapters_new.replace(str_to_replace, str_replacement)
    
    # 3. User manual
    expand = ""
    if ("/user_manual/" in filename):
        expand = "expanded"
    str_to_replace="<li class=\"chapter-item expanded \"><div><strong aria-hidden=\"true\">3.</strong> User manual</div></li>"
    str_replacement=f"<li class=\"part-title {expand}\" id=\"li-user-manual\"><button class=\"button-summary\" id=\"button-user-manual\" title=\"User Manual\"><strong aria-hidden=\"true\"><i class=\"fa fa-chevron-right\" id=\"chevron-user-manual\"></i>&nbsp;&nbsp;User manual&nbsp;&nbsp;<i class=\"fa fa-book\"></i></strong></button></li>"
    chapters_new = chapters_new.replace(str_to_replace, str_replacement)
    
    # 4. Community
    expand = ""
    if ("/community/" in filename):
        expand = "expanded"
    str_to_replace="<li class=\"chapter-item expanded \"><div><strong aria-hidden=\"true\">4.</strong> Community</div></li>"
    str_replacement=f"<li class=\"part-title {expand} \" id=\"li-community\"><button class=\"button-summary\" id=\"button-community\" title=\"Community\"><strong aria-hidden=\"true\"><i class=\"fa fa-chevron-right\" id=\"chevron-community\"></i>&nbsp;&nbsp;Community&nbsp;&nbsp;<i class=\"fa fa-comments\"></i></strong></button></li>"
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