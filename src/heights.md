# Tiles heights

This section covers tiles and collisions heights ! 

> 🐞 [Bug tracker here](https://trello.com/b/PIzgsYov/rpg-power-forge-road-map)

---
## Open the Tile Height Setter

You can open the **Tile Height Setter** from the **Window** top menu.

![top_menu_access.png](./../media/heights/top_menu_access.png)

---
## Tile Height Setter Window

The **Tile Height Setter** window has few sections :
* A "toggle visibility" button
* A set of tool to apply height to tiles easily
* A tilemap selector (same as the **Tile Palette**)
* A height selection, from 0 (lower) to 9 (higher)

![tile_height_setter_window.png](./../media/heights/tile_height_setter_window.png)

---
## Apply the height of tiles manually

It's quite simple actually !

![apply_height_to_tiles.gif](./../media/heights/apply_height_to_tiles.gif)


## Apply the height of tiles automatically

*In developpement*

## How to go above and below ?

To change height of your playable character during play, you need to tell **RPG Power Forge** where the stairs are. This is where the **Stair prefab** comes in !

In the **[Asset Picker](./place_props.md)**, select the **Stair** prefab (under Built-In/LD). In our example, we are using the **TopDownStair** prefab.

![height_stair_prefab.gif](./../media/heights/height_stair_prefab.gif)

