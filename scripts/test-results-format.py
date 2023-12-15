
import re # regex operations
import sys # to return 0
import os # loop over files

# goal : edit the external links by removing ".html" at the end

# replace in a file
def set_test_results_format(filename):

    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    # PASS results
    str_to_replace = "<td>PASS</td>"
    str_replacement = f"<td style=\"color:black;background-color:LightGreen\">Passed</td>"
    s = s.replace(str_to_replace, str_replacement)

    # FAIL results
    str_to_replace = "<td>FAIL</td>"
    str_replacement = f"<td style=\"color:black;background-color:LightCoral\">Failed</td>"
    s = s.replace(str_to_replace, str_replacement)

    # NOT_TESTED results
    str_to_replace = "<td>NOT_TESTED</td>"
    str_replacement = f"<td style=\"color:black;background-color:LightGrey\">Not tested</td>"
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
book_root = "./../book/"
nb_files=0
print("====================================")
print("TESTS RESULTS FORMAT UPDATE")
print(f"Scanning html files in {book_root} and update tests results format")
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_test_results_format(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)