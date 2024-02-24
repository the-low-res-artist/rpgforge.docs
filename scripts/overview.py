
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
          <h3>Asset Picker</h3>\
          <p>Import, organize, edit, drag and drop all of your assets on the Scene !</p>\
        </div>\
      </div>\
      <div class=\"overview_toolbar overview\"> \
        <div class=\"panel_toolbar panel\">\
          <h3>Tool Bar</h3>\
          <p>Quick access to most RPG Power Forge features. Data, settings, build...</p>\
        </div>\
      </div>\
      <div class=\"overview_scene overview\"> \
        <div class=\"panel_scene panel\">\
          <h3>Scene</h3>\
          <p>This is where everything comes to life !</p>\
        </div>\
      </div>\
      <div class=\"overview_behavior overview\">\
        <div class=\"panel_behavior panel\">\
          <h3>Behaviors</h3>\
          <p>Attach multiple high-level RPG game behaviors to an Actor (prefab).</p>\
        </div>\
      </div>\
      <div class=\"overview_properties overview\"> \
        <div class=\"panel_properties panel\">\
          <h3>Properties</h3>\
          <p>Customize the settings for each Scene element (tiles, props, Actors, ...)</p>\
        </div>\
      </div>\
      <div class=\"overview_hierarchy overview\"> \
        <div class=\"panel_hierarchy panel\">\
          <h3>Hierarchy</h3>\
          <p>Select and reorganize your Scene elements (Actors, props, ...)</p>\
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