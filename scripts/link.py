
import re # regex operations
import sys # to return 0
import os # loop over files

# goal : edit the external links by removing ".html" at the end

# replace in a file
def set_link(filename):

    print(f"Updating {filename}...")

    LINK_REGEX = "(https?://.+?\.html)"
    HOSTS_LIST = ["trello.com", "x.com", "twitter.com"]

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # find all matches
    matches = re.findall(LINK_REGEX, s)

    # safe exit
    if (len(matches) == 0):
        return

    print("all link matches:")
    print(matches)
    for match in matches:
        host = match.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0]
        if host in HOSTS_LIST:
            print(f"matching host : {host}")
            str_to_replace = match
            str_replacement = str_to_replace.replace('.html', '')
            print(f"{str_to_replace} => {str_replacement}")
            print("---")
            s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
root = "./../book/"
print("====================================")
print("LINKS UPDATE")
print(f"Scanning html files in {root} and fixing external links suffixes")
for root, dirs, files in os.walk(root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_link(os.path.join(root, filename))

# safe return
sys.exit(0)