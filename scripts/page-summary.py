
import re # regex operations
import sys # to return 0
import os # loop over files
import time # measure duration

# goal : create a summary for each page (if the '## Summary' tag is used)

# replace in a file
def set_page_summary(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # search titles (example : '## Create a project on itchio')
    summary = ""
    with open(filename, 'r', encoding="utf8") as f:
        for line in f.readlines():
            # remove last \n
            line=line[:-1]
            #skip summary itself
            if (line == "## Summary"):
                continue
            # initialisation
            title=""
            offset=0
            # test title
            if line.startswith("## "):
                title=line[3:]
            if line.startswith("### "):
                title=line[4:]
                offset=4
            if line.startswith("#### "):
                title=line[5:]
                offset=8
            # append title (if found)
            if (len(title) > 0):
                link=title.lower().replace(" ","-").replace("(","").replace(")","")
                summary += ' '*offset + f"- [{title}](#{link})" + os.linesep

    # update summary (if found)
    if (len(summary) > 0):
        str_to_replace = '## Summary'
        str_replacement = '## Summary' + os.linesep + summary
        s = s.replace(str_to_replace, str_replacement)

        # Safely write the changed content
        with open(filename, 'w', encoding="utf8") as f:
            f.write(s)

# entry point
start = time.time()
src_root = "./../src/"
nb_files=0
for root, dirs, files in os.walk(src_root, topdown=False):
   for filename in files:
        if filename.endswith(".md"):
            set_page_summary(os.path.join(root, filename))
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] PAGE SUMMARY UPDATE : {nb_files} updated")

# safe return
sys.exit(0)