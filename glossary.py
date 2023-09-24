
import re

# goal : to find and replace each glossary entry with a tooltip (mouse hover)
# example : ?Pivot? ==> [<span style="color:orange">Pivot</span>][pivot]

# constants
GLOSSARY_COLOR="orange"
GLOSSARY_REGEX=r"(\?(\w+)\?)"

# replace in a file
def set_glossary(filename):

    global GLOSSARY_COLOR
    global GLOSSARY_REGEX

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r') as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # find all matches
    matches = re.findall(GLOSSARY_REGEX, s)

    # safe exit
    if (len(matches) == 0):
        return

    print(matches)
    for match in matches:
        str_to_replace=match[0]
        word=match[1]
        glossary_entry=word.lower()

        str_replacement=f"[<span style=\"color:{GLOSSARY_COLOR}\">{word}</span>][{glossary_entry}]"
        print(str_to_replace)
        print(str_replacement)

        s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w') as f:
        f.write(s)


# entry point
set_glossary("./src/front_page.md")