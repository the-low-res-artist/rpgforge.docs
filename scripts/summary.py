
import re # regex operations
import sys # to return 0
import os # loop over files

# goal : create a summary for each page (if the '## Summary' tag is used)

# replace in a file
def set_summary(filename):

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
                link=title.lower().replace(" ","-")
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
src_root = "./../src/"
nb_files=0
print("====================================")
print("SUMMARY UPDATE")
print(f"Scanning md files in {src_root} and updating their summary section")
for root, dirs, files in os.walk(src_root, topdown=False):
   for filename in files:
        if filename.endswith(".md"):
            set_summary(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)