# Tiles heights

This section covers tiles and collisions heights ! 

> 🐞 [Bug tracker here](https://trello.com/b/PIzgsYov/rpg-power-forge-road-map)

## Summary
- [Window location](#window-location)
- [Window content](#window-content)
- [Apply the height of tiles manually](#apply-the-height-of-tiles-manually)
- [Apply the height of tiles automatically](#apply-the-height-of-tiles-automatically)
    - [The Fill tool](#the-fill-tool)
- [How to go above and below](#how-to-go-above-and-below)
    - [The Hammer tool](#the-hammer-tool)
    - [The Stair prefab](#the-stair-prefab)
    - [Demonstration](#demonstration)
- [Add custom collisions](#add-custom-collisions)

## Window location

You can open the **Tile Height Setter** from the **Window** top menu.

![top_menu_access.png](./../media/heights/top_menu_access.png)


## Window content

The **Tile Height Setter** window has few sections :
* A "toggle visibility" button
* A set of tool to apply height to tiles easily
* A tilemap selector (same as the **Tile Palette**)
* A height selection, from 0 (lower) to 9 (higher)

![tile_height_setter_window.png](./../media/heights/tile_height_setter_window.png)


## Apply the height of tiles manually

It's quite simple actually !

![apply_height_to_tiles.gif](./../media/heights/apply_height_to_tiles.gif)


## Apply the height of tiles automatically

You can always select you tile and a specificheight when drawing !

![height_auto.gif](./../media/heights/height_auto.gif)

### The Fill tool

The **Fill** tool speedup your workflow when editingthe whole height of a specific tile/autotile :

![height_fill.gif](./../media/heights/height_fill.gif)

## How to go above and below

### The Hammer tool

Start by breaking breaking some autotiles collisions. To do so, use the *Hammer** tool in the **Tile Palette** window, and click on any tile collision :

![break_collision.gif](./../media/heights/break_collision.gif)

> 🐲 The **Hammer** is cool! \<CTRL+Z\> or *hammer-click* again too re-apply the tile collision.

### The **Stair** prefab

To change height of your playable character during play, you need to tell **RPG Power Forge** where the stairs are. This is where the **Stair prefab** comes in !

In the **[Asset Picker](./place_props.md)**, select the **Stair** prefab (under Built-In/LD). In our example, we are using the **TopDownStair** prefab.

![height_stair_prefab.gif](./../media/heights/height_stair_prefab.gif)

> 🐲 Hold \<CTRL\> key went dragging a prefab to align it with the grid !

### Demonstration

![demo.gif](./../media/heights/demo.gif)

## Add custom collisions

Good ! But it could be better... We should add some collisions to prevent our character from running below everything. Let's utilize the **Custom colliders** prefabs !

![custom_collisions.gif](./../media/heights/custom_collisions.gif)

> 🐲 Make sure the custom collider is at the correct height ! Use the **[Properties](./properties.md)** window to check that. In our example, the collider should be at height 0 :

![properties_height.png](./../media/heights/properties_height.png)

Much better now !

![demo3.gif](./../media/heights/demo3.gif)
