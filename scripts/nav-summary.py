import re # regex operations
import sys # to return 0
import os # loop over files
import shutil # move files

# goal : update the navigation summary on each html page

# replace in a file
def set_nav_summary(filename):
    
    # define regex
    CHAPTERS_SECTION_REGEX = "(<ol class=\"chapter\">.*</ol>)"
    
    # Safely read the input filename using 'with'
    s= ""
    with open(filename, 'r', encoding="utf8") as f:
        s = f.read()

    # safe exit
    if (s == ""):
        return

    #chapter sample
    #<ol class="chapter"><li class="chapter-item expanded affix "><a href="front_page.html">Home</a></li><li class="chapter-item expanded affix "><li class="part-title">&gt; Installation</li><li class="chapter-item hidden expanded "><div><strong aria-hidden="true">1.</strong> HIDE</div></li><li><ol class="section"><li class="chapter-item expanded "><a href="download.html"><strong aria-hidden="true">1.1.</strong> Download</a></li><li class="chapter-item expanded "><a href="new_project.html"><strong aria-hidden="true">1.2.</strong> Create a new project</a></li><li class="chapter-item expanded "><a href="update.html"><strong aria-hidden="true">1.3.</strong> Update RPG Power Forge</a></li></ol></li><li class="chapter-item expanded "><li class="part-title">&gt; Getting started</li><li class="chapter-item hidden expanded "><div><strong aria-hidden="true">2.</strong> HIDE</div></li><li><ol class="section"><li class="chapter-item expanded "><div><strong aria-hidden="true">2.1.</strong> First 2D map !</div></li><li><ol class="section"><li class="chapter-item expanded "><a href="new_map.html"><strong aria-hidden="true">2.1.1.</strong> Create a map</a></li><li class="chapter-item expanded "><a href="place_tiles.html"><strong aria-hidden="true">2.1.2.</strong> Place tiles</a></li><li class="chapter-item expanded "><a href="new_layer.html"><strong aria-hidden="true">2.1.3.</strong> Add tiles layers</a></li><li class="chapter-item expanded "><a href="place_props.html"><strong aria-hidden="true">2.1.4.</strong> Place props</a></li><li class="chapter-item expanded "><a href="collision.html"><strong aria-hidden="true">2.1.5.</strong> Add collisions </a></li><li class="chapter-item expanded "><a href="heights.html"><strong aria-hidden="true">2.1.6.</strong> Tiles and collisions heights</a></li><li class="chapter-item expanded "><a href="properties.html"><strong aria-hidden="true">2.1.7.</strong> Properties</a></li></ol></li><li class="chapter-item expanded "><div><strong aria-hidden="true">2.2.</strong> Add content</div></li><li><ol class="section"><li class="chapter-item expanded "><a href="prefab_creation.html"><strong aria-hidden="true">2.2.1.</strong> Create and add prefabs</a></li></ol></li><li class="chapter-item expanded "><div><strong aria-hidden="true">2.3.</strong> Test your game</div></li><li><ol class="section"><li class="chapter-item expanded "><a href="play_mode.html"><strong aria-hidden="true">2.3.1.</strong> Play mode</a></li></ol></li><li class="chapter-item expanded "><div><strong aria-hidden="true">2.4.</strong> Export your game</div></li><li><ol class="section"><li class="chapter-item expanded "><a href="export_to_itchio.html"><strong aria-hidden="true">2.4.1.</strong> To itch.io</a></li></ol></li></ol></li><li class="chapter-item expanded "><li class="part-title">&gt; User manual</li><li class="chapter-item hidden expanded "><div><strong aria-hidden="true">3.</strong> HIDE</div></li><li><ol class="section"><li class="chapter-item expanded "><div><strong aria-hidden="true">3.1.</strong> Import assets</div></li><li><ol class="section"><li class="chapter-item expanded "><a href="import_spritesheet.html"><strong aria-hidden="true">3.1.1.</strong> Import animations</a></li><li class="chapter-item expanded "><a href="import_sprites.html"><strong aria-hidden="true">3.1.2.</strong> Import props</a></li><li class="chapter-item expanded "><a href="import_tileset.html"><strong aria-hidden="true">3.1.3.</strong> Import tiles</a></li></ol></li><li class="chapter-item expanded "><div><strong aria-hidden="true">3.2.</strong> Game mecanics</div></li><li><ol class="section"><li class="chapter-item expanded "><a href="prefab_bahaviors.html"><strong aria-hidden="true">3.2.1.</strong> Prefab behaviors</a></li><li><ol class="section"><li class="chapter-item expanded "><a href="prefab_bahaviors_move.html"><strong aria-hidden="true">3.2.1.1.</strong> Move</a></li><li class="chapter-item expanded "><a href="prefab_bahaviors_attack.html"><strong aria-hidden="true">3.2.1.2.</strong> Attack</a></li></ol></li></ol></li><li class="chapter-item expanded "><div><strong aria-hidden="true">3.3.</strong> More</div></li><li><ol class="section"><li class="chapter-item expanded "><a href="code.html"><strong aria-hidden="true">3.3.1.</strong> Explore the code</a></li><li class="chapter-item expanded "><a href="about.html"><strong aria-hidden="true">3.3.2.</strong> About the project</a></li><li class="chapter-item expanded "><a href="functional_tests.html"><strong aria-hidden="true">3.3.3.</strong> Functional tests</a></li><li class="chapter-item expanded "><a href="performance_tests.html"><strong aria-hidden="true">3.3.4.</strong> Performance tests</a></li></ol></li></ol></li><li class="chapter-item expanded "><li class="part-title">&gt; Community</li><li class="chapter-item hidden expanded "><div><strong aria-hidden="true">4.</strong> HIDE</div></li><li><ol class="section"><li class="chapter-item expanded "><div><strong aria-hidden="true">4.1.</strong> Dev Team</div></li><li class="chapter-item expanded "><div><strong aria-hidden="true">4.2.</strong> Discord channel</div></li><li class="chapter-item expanded "><a href="https://twitter.com/RPGPowerForge"><strong aria-hidden="true">4.3.</strong> Twitter</a></li><li class="chapter-item expanded "><a href="https://trello.com/b/PIzgsYov/rpg-power-forge-road-map"><strong aria-hidden="true">4.4.</strong> Road map</a></li><li class="chapter-item expanded "><div><strong aria-hidden="true">4.5.</strong> Included assets</div></li></ol></li></ol>

    # get the chapters in the nav section
    chapters = re.findall(CHAPTERS_SECTION_REGEX, s)[0]
    chapters_new = chapters
    # safe exit
    if (len(chapters) == 0):
        return

    # reformat some chapters

    # Home
    str_to_replace="<li class=\"chapter-item expanded affix \"><a href=\"front_page.html\" tabindex=\"0\">Home</a></li>"
    str_replacement="<li class=\"part-title expanded affix \"><a href=\"front_page.html\" tabindex=\"0\"><i class=\"fa fa-house\"></i> Home</a></li>"
    chapters_new = chapters_new.replace(str_to_replace, str_replacement)
    # 1. Installation
    #str_to_replace="<li class=\"chapter-item expanded \"><div><strong aria-hidden=\"true\">1.</strong> Installation 📦</div></li>"
    #str_replacement="<li class=\"part-title expanded \"><div><strong aria-hidden=\"true\"><i class=\"fa fa-chevron-down\"></i> Installation 📦</strong></div></li>"
    #chapters_new = chapters_new.replace(str_to_replace, str_replacement)
    # 2. Getting started
    #str_to_replace="<li class=\"chapter-item expanded \"><div><strong aria-hidden=\"true\">2.</strong> Getting started ↗️</div></li>"
    #str_replacement="<li class=\"part-title \"><div><strong aria-hidden=\"true\"><i class=\"fa fa-chevron-right\"></i> Getting started ↗️</strong></div></li>"
    #chapters_new = chapters_new.replace(str_to_replace, str_replacement)
    # 3. User manual
    #str_to_replace="<li class=\"chapter-item expanded \"><div><strong aria-hidden=\"true\">3.</strong> User manual 📕</div></li>"
    #str_replacement="<li class=\"part-title \"><div><strong aria-hidden=\"true\"><i class=\"fa fa-chevron-right\"></i> User manual 📕</strong></div></li>"
    #chapters_new = chapters_new.replace(str_to_replace, str_replacement)
    # 4. Community
    #str_to_replace="<li class=\"chapter-item expanded \"><div><strong aria-hidden=\"true\">4.</strong> Community 😊</div></li>"
    #str_replacement="<li class=\"part-title \"><div><strong aria-hidden=\"true\"><i class=\"fa fa-chevron-right\"></i> Community 😊</strong></div></li>"
    #chapters_new = chapters_new.replace(str_to_replace, str_replacement)

    # update the nav section (chapters)
    str_to_replace = chapters
    str_replacement = chapters_new
    s = s.replace(str_to_replace, str_replacement)

    # Safely write the changed content
    with open(filename, 'w', encoding="utf8") as f:
        f.write(''.join(s))

# entry point
book_root = "./../book/"
nb_files=0
print("====================================")
print("NAV SUMMARY UPDATE")
print(f"Scanning html files in {book_root} and update the navigation summary section")
for root, dirs, files in os.walk(book_root, topdown=False):
   for filename in files:
        if filename.endswith(".html"):
            set_nav_summary(os.path.join(root, filename))
            nb_files+=1
print(f"{nb_files} updated")

# safe return
sys.exit(0)