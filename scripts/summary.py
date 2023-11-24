
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

    ## Summary
    - [Create a project on itchio](#create-a-project-on-itchio)
        - [Verify your mail adress](#verify-your-mail-adress)
        - [Create a new project page](#create-a-new-project-page)
    - [Export your game to itchio](#export-your-game-to-itchio)

    # search titles (example : '## Create a project on itchio')
    summary = ""
    for line in s:
        if line.startswith("## "):
            title=line[3:]
            link=title.lower().replace(" ","-")
            summary += f"- [{title}](#{link})" + os.linesep
        if line.startswith("### "):
            title=line[4:]
            link=title.lower().replace(" ","-")
            summary += f"    - [{title}](#{link})" + os.linesep

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
print(f"Scanning md files in {src_root} and updating their glossary words")
for root, dirs, files in os.walk(src_root, topdown=False):
   for filename in files:
        if filename.endswith(".md"):
            set_summary(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)