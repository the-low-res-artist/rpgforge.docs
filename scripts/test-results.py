import re # regex operations
import sys # to return 0
import os # loop over files
import json # move files

# goal : create a .md file from the Unity tests results

# helper
def get_result(result_dict, key):

    # remove the entries dict level
    result_dict = result_dict['entries']

    for result in result_dict:
        if result['key'] == key:
            return result['value']
    return ""

# generate the md file from the results
def generate_results_md(requirements_file, results_file, output_file):

    PASS="Passed"
    FAIL="Fail"
    NOT_TESTED="Not_tested"

    # Safely read the requirements filename using 'with'
    requirements= ""
    with open(requirements_file, 'r', encoding="utf8") as f:
        requirements = f.readlines()
    
    # Safely read the results test filename using 'with'
    results_data= {}
    with open(results_file, 'r', encoding="utf8") as f:
        results_data = json.load(f)
    
    # requirements details and results
    requirements_data={}
    for req in requirements:
        # clear the req line from '\r' '\n' and split it by ';'
        tab = req.strip().rstrip().split(';')
        req_id = tab[0]
        req_feat = tab[1]
        req_desc = tab[2]
        req_result = get_result(results_data, req_id)
        if not req_result in f"{PASS};{FAIL};{NOT_TESTED}" or len(req_result) == 0:
            req_result = NOT_TESTED
        requirements_data[req_id] = {"id": req_id, "feature": req_feat, "description": req_desc, "result" : req_result}
    
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
        if not req_result in f"{PASS};{FAIL};{NOT_TESTED}":
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

    # results summary
    total_req = 0
    total_req_passed = 0
    total_req_fail = 0
    total_req_not_tested = 0
    # count req results categories (total and passed)
    for req_id in requirements_data:
        total_req += 1
        req_result = requirements_data[req_id]["result"]
        if req_result == PASS:
            total_req_passed += 1
        elif req_result == FAIL:
            total_req_fail += 1
        elif req_result == NOT_TESTED:
            total_req_not_tested += 1
    # default summary
    if total_req_passed == total_req:
        results_summary_icon = "check"
        results_summary_title= "Oh yeah"
        results_summary_text = "All requirements passed ✔️ !"
    elif total_req_passed < total_req and total_req_fail == 0:
        results_summary_icon = "check"
        results_summary_title= "Oh yeah"
        results_summary_text = "All tested requirements passed ✔️ !"
    elif total_req_passed < total_req and total_req_fail > 0:
        ratio = total_req_passed/(float(total_req_passed) + total_req_fail)
        ratio = round(ratio * 100, 1)
        results_summary_icon = "warning"
        results_summary_title= "Testing ..."
        results_summary_text = f"{ratio}% of tested requirements passed ✔️ !"
    s = f"# Requirements \n\
This section list each ?requirement? for RPG Power Forge features as well as their tests results.\n\
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
|Item|Value|\n\
---|---\n\
RPG Power Forge version|{get_result(results_data, 'rpf_version')}\n\
Unity Editor version| {get_result(results_data, 'unity_version')}\n\
Host OS|{get_result(results_data, 'host_OS')}\n\
Host spec|{get_result(results_data, 'host_spec')}\n\
Date|{get_result(results_data, 'date')}\n\
\n\
## Tests results\n\
\n\
Feature|Passed ✔️|Failed ❌|Not tested yet...\n\
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
results_file="./../tests/results.json"

generate_results_md(requirements_file, results_file, output_file)
print(f"TESTS RESULTS UPDATE : {output_file} generated")

# safe return
sys.exit(0)