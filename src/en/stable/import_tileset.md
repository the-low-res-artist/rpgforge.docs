# Import a tileset

This section covers the import of a tileset into **RPG Power Forge**.

> 🐞 [Bug tracker here](https://trello.com/b/PIzgsYov/rpg-power-forge-road-map)


## Summary

## Recommendations

First, you should check if the default resolution property match the tileset you want to import. Project properties are located under the **RPG Power Forge** top-menu.

![project_location.png](./../media/place_tiles/project_location.png)

The property **Pixel per Unit** should match the resolution of the tiles you are importing (16 is default for a 16x16 resolution tileset).

![ppu.png](./../media/place_tiles/ppu.png)

> 🐲 Weird results if not match accordingly !

Other recommendations :

- At any time, you can hit the **[Back Button]** to cancel current edit and go back to the previous UI panel :

![back_arrow.png](./../media/import/back_arrow.png)
- You can import a set of free resources here : [resources.zip](./../media/zip/resources.zip)
- If you quit the UI during the import without (with the top-right❌button), nothing will be saved and you will need to restart the import.

## Window location

To import tiles, you need to access the **Import Assets** User Interface (UI). It is located under the **RPG Power Forge** menu.

![import_button.png](./../media/import/import_button.png)

## Window content

The UI let you choose what kind of assets you want to import.

![import_ui.png](./../media/import/import_ui.PNG)

## Import Tiles

You can import a set of tiles in **[RPG Power Forge]**. Let's try with the following sample (a 16x16 resolution tileset file) : *Download this file to import it in the next steps*

![tileset.png](./../media/import/tileset.png)

> 🐲 This file is also accessible in the free resources archive linked in the above [Recommendations](#recommendations) section.

To import this tileset, select **[Tiles]**

![import_select_tiles.png](./../media/import/import_select_tiles.png)

Then **[Tileset]**

![import_select_tileset.png](./../media/import/import_select_tileset.PNG)

The explorer opens, asking you to select the file itself. Here we will select the tileset.png shown above. Once selected, the tileset is loaded in the UI.

![import_properties_tileset.png](./../media/import/import_properties_tileset.PNG)


### Slice Tiles

To create tiles in **Unity** we first need to serapate each tile individually. This operation is called **[Slice]**.

Select **[Slice]** in the UI to be able to slice your tileset into tiles according to the following properties.

Property|Type|Function|Example
--------|--------|--------|--------
Method|Enum|Slice method (Pixel Size or Column & Rows numbers)| Pixel Size
Pixel Size|Integer|X and Y sizes (in pixel) of a tile on the tileset|[16;20]
Row & Column |Integer|number of rows and columns of tiles on the tileset|[16;16]

![import_slice_tileset.png](./../media/import/import_slice_tileset.PNG)

### Set Transparent Colors

*In developpement*

### Remove Empty Sprites

This action detects empty tiles (with only transparent pixels) and removes them before the tiles are loaded in **RPG Power Forge**.


### Template

If your tileset follows a RPG Maker convention (autotiles), you can slice it automatically with a template ! For example :

![import_template.png](./../media/import/import_template.png)

Property|Function
--------|--------|
RM MV-MZ-VX A1|Template for animated autotiles
RM MV-MZ-VX A2|Template for floor autotiles
RM MV-MZ-VX A3|Template for roof and wall autotiles
RM MV-MZ-VX A4|Template for floor and wall autotiles

> 🐲 Templates are super useful for quick RPG Maker-compatible autotile import !


### Apply

Once you are OK, press **[Apply]** to validate your setup. Your tileset will be located in *Assets/Project/Sprites* folder.


## Edit tiles

The next UI allows you to edit each tile and define if they need a collision.

Select a tile in the UI to access its properties on the left panel. You can tick the option **[Generate Collissions]** ☑️ to create a custom collision.

In the example below, we have selected the bush tile and added a collision to it.

![import_edit_tiles.png](./../media/import/import_edit_tiles.png)

Once you are OK, press **[Apply]**. Your tiles will be located in *Assets/Project/Tiles* folder.

![import_tile_collection_location.png](./../media/import/import_tile_collection_location.png)

> 🐲 This is a **Tile Collection**. Double-click this object in your Project window to edit your tiles if necessary !

{{#include glossary.md}}