
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

    svg = "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"16\" width=\"16\" viewBox=\"0 0 512 512\"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path fill=\"#ffffff\" d=\"M320 0c-17.7 0-32 14.3-32 32s14.3 32 32 32h82.7L201.4 265.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L448 109.3V192c0 17.7 14.3 32 32 32s32-14.3 32-32V32c0-17.7-14.3-32-32-32H320zM80 32C35.8 32 0 67.8 0 112V432c0 44.2 35.8 80 80 80H400c44.2 0 80-35.8 80-80V320c0-17.7-14.3-32-32-32s-32 14.3-32 32V432c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16V112c0-8.8 7.2-16 16-16H192c17.7 0 32-14.3 32-32s-14.3-32-32-32H80z\"/></svg>"

    str_to_replace = "OVERVIEW_GO_HERE"
    str_replacement = f"<div class=\"overview_container\">\
    <div class=\"overview_panel\"> \
    </div>\
    <div class=\"overview_unity_editor\"> \
      <div class=\"overview_asset_picker overview\"> \
        <div class=\"panel_asset_picker panel\"  onclick=\"window.location.href = 'https://rpgpowerforge.com/en/stable/user_manual/assets_management/assets_picker/assets_picker.html';\" style=\"cursor: pointer;\">\
          <h4>🌳 Assets {svg}</h4>\
          <p>Import, organize, edit and drop all of your assets in the Scene !</p>\
        </div>\
      </div>\
      <div class=\"overview_toolbar overview\"> \
        <div class=\"panel_toolbar panel\" onclick=\"window.location.href = 'https://rpgpowerforge.com/en/stable/user_manual/quality_of_life/toolbar.html';\" style=\"cursor: pointer;\">\
          <h4>💡 Tool Bar {svg}</h4>\
          <p>Quick access to most RPG Power Forge features. Data, settings, build...</p>\
        </div>\
      </div>\
      <div class=\"overview_scene overview\"> \
        <div class=\"panel_scene panel\" onclick=\"window.location.href = 'https://rpgpowerforge.com/en/stable/user_manual/game_mecanics/scene_creation/scene_creation.html';\" style=\"cursor: pointer;\">\
          <h4>🎬 Scene {svg}</h4>\
          <p>This is where everything comes to life ! Create a Scene and play instantly.</p>\
        </div>\
      </div>\
      <div class=\"overview_behavior overview\">\
        <div class=\"panel_behavior panel\">\
          <h4>⚔️ Behavior {svg}</h4>\
          <p>Attach multiple high-level RPG game behaviors to an Actor (prefab).</p>\
        </div>\
      </div>\
      <div class=\"overview_properties overview\"> \
        <div class=\"panel_properties panel\">\
          <h4>⚙️ Property {svg}</h4>\
          <p>Customize the settings for each Scene element (Tiles, Props, Actors, ...)</p>\
        </div>\
      </div>\
      <div class=\"overview_hierarchy overview\"> \
        <div class=\"panel_hierarchy panel\">\
          <h4>📂 Hierarchy</h4>\
          <p>Select and reorganize your Scene elements (Tiles, Props, Actors, ...)</p>\
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