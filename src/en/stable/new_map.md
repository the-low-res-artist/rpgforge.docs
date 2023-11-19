# Map

This section covers the creation of a new map (as known as *Scene* in **Unity**) :

> 🐞 [Bug tracker here](https://trello.com/b/PIzgsYov/rpg-power-forge-road-map)

## Summary
- [Window location](#window-location)
- [Window content](#window-content)

## Window location

To create a new map, simply open the **RPG Power Forge** menu :

![create_map.png](./../media/map/create_map.png)

## Window content

Map creation has a few properties :

![create_map_settings.png](./../media/map/create_map_settings.png)


Property|Type|Function|Example
--------|--------|--------|--------
Name|String|Name of the map. Will serve as a filename for the .scene file| "new_map" or "my map 001"
Template|Enum|    Type of level you want to load    |Sample Top Down Level
Camera|Enum|    Type of camera to use to render the map    |DefaultTopDownCamera
Avatar|Enum|    Type of the playable character to instanciate on the map    |DefaultTopDownAvatarParameters

Select **[Create]** to create a new map.

![create_map_layers.png](./../media/map/create_map_layers.png)

 Once the map is created, you will see a default object added :
* [Root] object: every tile layers are attached to it
    * [Tilemap] object : a first layer to draw tiles ([how to add more](./new_layer.md))
    * [Start] object : where the player is instanciate in Play Mode.


{{#include glossary.md}}