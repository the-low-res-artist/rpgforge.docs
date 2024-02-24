
import re # regex operations
import sys # to return 0
import os # loop over files
from config import config
import time # measure duration

# goal : edit home to add specific div tags

# replace in a file
def set_overview(filename):
    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    str_to_replace = "OVERVIEW_GO_HERE"
    str_replacement = f"<div class=\"overview_container\">\
    <div class=\"overview_panel\"> \
    </div>\
    <div class=\"overview_unity_editor\"> \
      <div class=\"overview_asset_picker overview\"> \
        <div class=\"panel_asset_picker panel\">\
          <h2>Asset Picker</h2\>\
          <p>Import, edit, drag and drop various assets on the Scene ! Perfect for prefabs and tiles management.</p>\
        </div>\
      </div>\
      <div class=\"overview_toolbar overview\"> \
        <div class=\"panel_toolbar panel\">\
          <h2>Tool Bar</h2>\
          <p>Quick access to most RPG Power Forge features. Data management, project settings, game build and more !</p>\
        </div>\
      </div>\
      <div class=\"overview_scene overview\"> \
        <div class=\"panel_scene panel\">\
          <h2>Scene</h2>\
          <p>Customize the settings for each Scene element (tiles, props, actors, ...)</p>\
        </div>\
      </div>\
      <div class=\"overview_behavior overview\">\
        <div class=\"panel_behavior panel\">\
          <h2>Behaviors</h2>\
          <p>Attach any high-level RPG behaviors to an Actor (prefab).</p>\
        </div>\
      </div>\
      <div class=\"overview_properties overview\"> \
        <div class=\"panel_properties panel\">\
          <h2>Properties</h2>\
          <p>Customize the settings for each Scene element (tiles, props, actors, ...)</p>\
        </div>\
      </div>\
      <div class=\"overview_hierarchy overview\"> \
        <div class=\"panel_hierarchy panel\">\
          <h2>Hierarchy</h2>\
          <p>Select and reorganize your Scene elements (actors, props, ...)</p>\
        </div>\
      </div>\
    </div>\
    <div class=\"overview_panel\">\
    </div>\
</div>"
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(s)


# entry point
start = time.time()
book_root = "./../book/"
nb_files=0

for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            basename = os.path.basename(filename)
            if ("rpg_power_forge_overview.html"):
                set_overview(os.path.join(root, filename))
            nb_files+=1

end = time.time()
print(f"[{str(round(end - start, 1))} sec] OVERVIEW UPDATE : {nb_files} updated")

# safe return
sys.exit(0)