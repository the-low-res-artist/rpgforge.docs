
import re # regex operations
import sys # to return 0
import os # loop over files

# goal : to find and replace each glossary entry with a tooltip (mouse hover)
# example : ?Pivot? ==> [<span style="color:orange">Pivot</span>][pivot]

# constants
GLOSSARY_COLOR="orange"
GLOSSARY_REGEX=r"(\?(\w+)\?)"

# replace in a file
def set_glossary(filename):

    print(f"Updating {filename}...")

    global GLOSSARY_COLOR
    global GLOSSARY_REGEX

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # find all matches
    matches = re.findall(GLOSSARY_REGEX, s)

    # safe exit
    if (len(matches) == 0):
        return

    for match in matches:
        str_to_replace=match[0]
        word=match[1]
        glossary_entry=word.lower()
        str_replacement="[<span style=\"color:" + GLOSSARY_COLOR + "\">" + word + "</span>][" + glossary_entry + "]"
        s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
root = "./../src/"
print("====================================")
print("GLOSSARY UPDATE")
print(f"Scanning md files in {root} and updating their glossary words")
for root, dirs, files in os.walk(root, topdown=False):
   for filename in files:
        if filename.endswith(".md"):
            set_glossary(os.path.join(root, filename))

# safe return
sys.exit(0)