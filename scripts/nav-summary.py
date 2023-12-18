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
    str_to_replace="\">Home</a></li>"
    str_replacement="\">Home <i class=\"fa fa-home\"></i></a></li>"
    chapters_new = chapters_new.replace(str_to_replace, str_replacement)
    
    str_to_replace="<ol class=\"chapter\"><li class=\"chapter-item"
    str_replacement="<ol class=\"chapter\"><li class=\"part-title"
    chapters_new = chapters_new.replace(str_to_replace, str_replacement)
    
    # 1. Installation
    expand = ""
    chevron_icon_class="fa fa-chevron-right"
    if ("/installation/" in filename):
        expand = " expanded"
        chevron_icon_class="fa fa-chevron-down"
    str_to_replace="<li class=\"chapter-item expanded \"><div><strong aria-hidden=\"true\">1.</strong> Installation</div></li>"
    str_replacement=f"<li class=\"part-title{expand}\" id=\"li-installation\"><button class=\"button-summary\" id=\"button-installation\" title=\"Installation\"><strong aria-hidden=\"true\"><i class=\"{chevron_icon_class}\" id=\"chevron-installation\"></i>&nbsp;&nbsp;Installation&nbsp;&nbsp;</strong></button></li>"
    chapters_new = chapters_new.replace(str_to_replace, str_replacement)
    
    # 2. Getting started
    expand = ""
    chevron_icon_class="fa fa-chevron-right"
    if ("/getting_started/" in filename):
        expand = " expanded"
        chevron_icon_class="fa fa-chevron-down"
    str_to_replace="<li class=\"chapter-item expanded \"><div><strong aria-hidden=\"true\">2.</strong> Getting started</div></li>"
    str_replacement=f"<li class=\"part-title{expand}\" id=\"li-getting-started\"><button class=\"button-summary\" id=\"button-getting-started\" title=\"Getting Started\"><strong aria-hidden=\"true\"><i class=\"{chevron_icon_class}\" id=\"chevron-getting-started\"></i>&nbsp;&nbsp;Getting started&nbsp;&nbsp;</strong></button></li>"
    chapters_new = chapters_new.replace(str_to_replace, str_replacement)
    
    # 3. User manual
    expand = ""
    chevron_icon_class="fa fa-chevron-right"
    if ("/user_manual/" in filename):
        expand = " expanded"
        chevron_icon_class="fa fa-chevron-down"
    str_to_replace="<li class=\"chapter-item expanded \"><div><strong aria-hidden=\"true\">3.</strong> User manual</div></li>"
    str_replacement=f"<li class=\"part-title{expand}\" id=\"li-user-manual\"><button class=\"button-summary\" id=\"button-user-manual\" title=\"User Manual\"><strong aria-hidden=\"true\"><i class=\"{chevron_icon_class}\" id=\"chevron-user-manual\"></i>&nbsp;&nbsp;User manual&nbsp;&nbsp;</strong></button></li>"
    chapters_new = chapters_new.replace(str_to_replace, str_replacement)
    
    # 4. Community
    expand = ""
    chevron_icon_class="fa fa-chevron-right"
    if ("/community/" in filename):
        expand = " expanded"
        chevron_icon_class="fa fa-chevron-down"
    str_to_replace="<li class=\"chapter-item expanded \"><div><strong aria-hidden=\"true\">4.</strong> Community</div></li>"
    str_replacement=f"<li class=\"part-title{expand}\" id=\"li-community\"><button class=\"button-summary\" id=\"button-community\" title=\"Community\"><strong aria-hidden=\"true\"><i class=\"{chevron_icon_class}\" id=\"chevron-community\"></i>&nbsp;&nbsp;Community&nbsp;&nbsp;</strong></button></li>"
    chapters_new = chapters_new.replace(str_to_replace, str_replacement)

    # 5. About the project
    expand = ""
    chevron_icon_class="fa fa-chevron-right"
    if ("/about/" in filename):
        expand = " expanded"
        chevron_icon_class="fa fa-chevron-down"
    str_to_replace="<li class=\"chapter-item expanded \"><div><strong aria-hidden=\"true\">5.</strong> About the project</div></li>"
    str_replacement=f"<li class=\"part-title{expand}\" id=\"li-about\"><button class=\"button-summary\" id=\"button-about\" title=\"About\"><strong aria-hidden=\"true\"><i class=\"{chevron_icon_class}\" id=\"chevron-about\"></i>&nbsp;&nbsp;About the project</strong></button></li>"
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