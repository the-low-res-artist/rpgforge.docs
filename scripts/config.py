# define global variables used in python pre and post build scripts
class config:

    # =============================================================================
    # =============================================================================
    # variables title
    doc_website_title = "RPG Power Forge"
    doc_website_subtitle = "documentation website"

    # =============================================================================
    # =============================================================================
    # variables to replace in md files
    md_variables = {
        "VAR_UNITY_HUB_MIN_VERSION" : "3.8",
        "VAR_UNITY_SHORT_MIN_VERSION" : "2022.3",
        "VAR_UNITY_MIN_VERSION" : "2022.3.34f1",
        "VAR_RPF_RECOMMENDED_VERSION" : "0.3.0",
        "TRELLO_WEBSITE_LINK": "https://trello.com/b/PIzgsYov/road-map"
    }

    # =============================================================================
    # =============================================================================
    # css files to include
    css_common_list = ["behavior_tags.css", 
                    "join-community.css", 
                    "footer.css", 
                    "main.css", 
                    "mdbook-admonish.css", 
                    "rating.css", 
                    "summary.css"]

    css_black_list = ["hero.css"]

    # =============================================================================
    # =============================================================================
    # installation page
    title_install_unity = "Install Unity"
    title_dl_rpgpowerforge = "Install RPG Power Forge"
    title_create_project = "Create a new project"
    
    tags_install_unity = ["Unity Hub", "Unity Editor"]
    tags_dl_rpgpowerforge = ["Unity package", "Unity Assets Store", "itch.io"]
    tags_create_project = ["it's easy", "I promise"]

    description_install_unity = "Unity is a cross-platform game engine."
    description_dl_rpgpowerforge = "RPG Power Forge is our product on top of Unity."
    description_create_project = "This is where the fun begins."

    # =============================================================================
    # =============================================================================
    # links for the nav bar
    link_x = "https://twitter.com/RPGPowerForge"
    link_discord = "https://onesquareminesweeper.com/"
    link_trello = "https://trello.com/b/PIzgsYov/road-map"
    link_youtube = "https://www.youtube.com/@rpgpowerforge"
    link_patreon = "https://www.patreon.com/rpgpowerforge/membership"
    link_kofi = "https://ko-fi.com/rpgpowerforge/tiers"
    # =============================================================================
    # =============================================================================
    # favicon
    img_favicon = "https://rpgpowerforge.com/media/icons/favicon5.png"

    # =============================================================================
    # =============================================================================
    # let's make a game !
    title_2d = "2D RPG game"
    title_3d = "3D RPG game"
    title_4d = "4D RPG game"

    tags_2d = ["simple", "accessible"]
    tags_3d = ["medium", "challenging"]
    tags_4d = ["impossible", "very_hard", "not_simple_at_all", "dont_try_this_at_home"]

    description_2d = "2D RPG games are cool and retro"
    description_3d = "Let do a 3D RPG game"
    description_4d = "???"

    # =============================================================================
    # =============================================================================
    # dev team
    title_gif = "Gif 👴🏻"
    title_chiw = "Chiw 😺"
    title_noiracide = "Noiracide 🎨"

    # html colors are choosen randomly haha (evil)
    tags_colors = ["BlueViolet", "Brown", "CornflowerBlue",
    "DarkGreen", "DarkRed", "Navy", "OrangeRed", "RoyalBlue", "Tomato",
    "Teal", "SlateGray", "Sienna", "PaleVioletRed", "DimGray"] 

    tags_gif = ["project_lead", "community_manager", "2d_artist", "website_builder", "too_much_tags", "documentation_writer", "marketing_enthousiast", "validation_tester"]
    tags_chiw = ["project_father", "C#_dev", "game_designer", "unit_tester"]
    tags_noiracide = ["project_father", "2d_artist", "3d_artist", "game_designer", "ui_ux_designer", "monkey_tester"]

    description_gif = "I love retrogaming !1!!§!"
    description_chiw = "I should make my game projects accessible to cats"
    description_noiracide = "I draw like a god but my sleep schedule is terrible"

    # =============================================================================
    # =============================================================================
    # terms to highlight
    highlight_terms = [
        'Unity Editor',
        'Unity Hub',
        'Unity',
        'RPG Power Forge',
        'Aseprite Importer',
        'Aseprite',
        'Probuilder',
        'Assets Importer',
        'Sprite Editor',
        'Sprite Sheet',
        'Sprite',
        'Slice',
        'Animation',
        'Prop',
        'Tile',
        'Collection'
    ]
        
        