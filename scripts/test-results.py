import re # regex operations
import sys # to return 0
import os # loop over files
import json # move files

# goal : create a .md file from the Unity tests results


# generate the md file from the results
def generate_results_md(requirements_file, results_folder, output_file):

    PASS="PASS"
    FAIL="FAIL"
    NOT_TESTED="NOT_TESTED"

    # Safely read the requirements filename using 'with'
    requirements= ""
    with open(requirements_file, 'r', encoding="utf8") as f:
        requirements = f.readlines()

    # Find most recent result file
    results_file_version="0.0.24RC11"
    results_filename="results_20231214_161100.json"
    
    # Safely read the results test filename using 'with'
    results_data= {}
    results_file=f"./../tests/{results_file_version}/{results_filename}"
    with open(results_file, 'r', encoding="utf8") as f:
        results_data = json.load(f)
    context_data = results_data["context"]

    # requirements details and results
    requirements_data={}
    for req in requirements:
        tab = req.split(';')
        req_id = tab[0]
        req_feat = tab[1]
        req_desc = tab[2]
        req_result = "NOT_TESTED"
        if req_id in results_data['results']:
            req_result = results_data['results'][req_id]
        requirements_data[req_id] = {"id": req_id, "feature": req_feat, "description": req_desc, "result" : req_result}

    # results summary
    results_summary_icon = "tip"
    results_summary_title="Oh yeah"
    results_summary_text = "All feature requirements are OK ✔️ !"
    
    # result by feature
    results_by_feature = ""
    results_by_feature_data = {}
    # initialize the dictionnary
    for req_id in requirements_data:
        feat = requirements_data[req_id]["feature"]
        results_by_feature_data[feat] = {PASS: 0, FAIL: 0, NOT_TESTED: 0, 'req_list': []}
    # fill the dictionnary per feature (count PASS, FAIL and NOT TESTED)
    for req_id in requirements_data:
        feat = requirements_data[req_id]["feature"]
        req_result = requirements_data[req_id]["result"]
        # skip if result is weird
        if not req_result in f"{PASS} {FAIL} {NOT_TESTED}":
            continue
        # save result overwise
        results_by_feature_data[feat][req_result] += 1
        # save the full req as well
        results_by_feature_data[feat]['req_list'].append(requirements_data[req_id])
    # fill the string result for the md file 
    for key, val in results_by_feature_data.items():
        feat_pass = results_by_feature_data[key][PASS]
        feat_fail = results_by_feature_data[key][FAIL]
        feat_not_tested = results_by_feature_data[key][NOT_TESTED]
        results_by_feature += f"{key}|{feat_pass}|{feat_fail}|{feat_not_tested}\n"

    # results details
    results_details = ""
    # fill the string detailled result for the md file 
    for key, val in results_by_feature_data.items():
        # skip if no requirements
        if len(results_by_feature_data[key]['req_list']) == 0:
            continue
        # begin feature section
        results_details += f"### {key} feature\n\
Requirement|Description|Test result\n\
---|---|---\n"
        # loop for req list
        for req in results_by_feature_data[key]['req_list']:
            results_details += f"{req['id']}|{req['description']}|{req['result']}\n"

    s = f"# Requirements \n\
This section list all of our ?technical requirements? for each RPG Power Forge feature as well as their tests results\n\
\n\
*(This page is under development)* \n\
\n\
```admonish {results_summary_icon} title=\"{results_summary_title}\" \n\
{results_summary_text}\n\
```\n\
\n\
## Summary\n\
\n\
## Context\n\
\n\
|||\n\
---|---\n\
RPG Power Forge version|{context_data['rpf_version']}\n\
Unity Editor version| {context_data['unity_version']}\n\
Host OS|{context_data['host_OS']}\n\
Host spec|{context_data['host_spec']}\n\
Date|{context_data['date']}\n\
\n\
## Tests results\n\
\n\
Feature|Passed ✔️|Failed ❌|Not tested 🍌\n\
---|---|---|---\n\
{results_by_feature}\n\
\n\
## Requirements details\n\
\n\
{results_details}\n"

    # Safely write the changed content
    with open(output_file, 'w', encoding="utf8") as f:
        f.write(s)

# ================================================================================
# entry point
output_file="./../src/en/stable/about/requirements.md"
requirements_file="./../requirements/requirements.csv"
results_folder="./../tests"

print("====================================")
print("TESTS RESULTS UPDATE")
print(f"Scanning the most recent test results to make a markdown file")
generate_results_md(requirements_file, results_folder, output_file)
print(f"{output_file} generated")

# safe return
sys.exit(0)