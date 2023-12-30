# Collision

This section covers collision ! Collision can be either :
* Assign to tiles and autotiles.
* Assign to props.
* Placed freely with custom shapes in the **[Asset Picker]** window.

> 🐞 [Bug tracker here](https://trello.com/b/PIzgsYov/rpg-power-forge-road-map)

## Summary

## Show or hide collisions in RPG Power Forge

At any point, you can toggle collision (hide/show). Just click the **[Markers]** icon 🚩.

![marker_location.png](./../media/collision/marker_location.png)


## Assign collisions to autotiles

If you already have placed tiles and props, your map could look like this (example).

![sample_no_collision.png](./../media/collision/sample_no_collision.PNG)

It needs collisions overwise your character will move freely ! To do so, you can edit your tiles, located in *Assets/Project/Tiles*. Let's edit the default autotile **[Tile Collection]** by double-clicking it. This collection is where the wood fence is.

![collision_tile_collection_location.png](./../media/collision/collision_tile_collection_location.png)

The **[Tile Collection]** window appears. Just select the Wood Fence autotile and tick the **[Generate Collisions]** chekcbox ☑️. Then, for this kind of autotile, choose *INNER* as the **[Collision Type]**.

![edit_tile_collision.png](./../media/collision/edit_tile_collision.PNG)

Collision Type|Function|
--------|--------
FULL|All of the tiles have collision
INNER|Only the inner part of the tiles (typically for fences).
OUTER|Only the outer part of the tiles.

> 🐲 Previews on the left side should help you set the collision as you want !

Once ready, select **[Apply]** button on the bottom-right of the window.

![sample_fence_collision.png](./../media/collision//sample_fence_collision.PNG)

All of the fences autotiles now have collision applied. Congratulations ! 


## Assign collisions to tiles

Like autotiles, you can assign collision to single tiles you have imported. Let's take a look at our tileset we have imported in a previous section. Double-click on the **[Tile Collection]** named *tileset*.

![import_tile_collection_location.png](./../media/import/import_tile_collection_location.png)

The **[Tile Collectio]n** edit window appears. Just select the "cut tree" tile and click the [Generate Collisions] ☑️. Then, for this kind of tile, choose *FULL* as the [Collision Type].

![edit_tile_2_collision.png](./../media/collision/edit_tile_2_collision.PNG)

Once ready, select [Apply]. Now everytime you will draw this tile on a layer, the collision will be applied.

![sample_trunk_collision.png](./../media/collision/sample_trunk_collision.PNG)


## Assign collisions to props

If you have some props, you can also set their collision from the **[Props Collection]** window. Let's try to add a few trees on a blank map then add collision to all of them in one click !

![add_collision_to_props.gif](./../media/collision/add_collision_to_props.gif)

## Add custom collision shapes freely

If needed, you can add custom collision shapes on your map. Just open the **[Asset Picker]** window.

![asset_picker_window_location.png](./../media/place_props/asset_picker_window_location.png)

Select the **[Colliders]** category (under *BuiltIn*) and choose a shape.

![colliders_location.png](./../media/collision/colliders_location.PNG)

Collider shape|Function|
--------|--------
Box|Rectangle shape
Circle|Circle shape
Edge|Line shape. You add and remove points on it
Polygon|Custom polygon shape

![colliders_shapes.png](./../media/collision/colliders_shapes.PNG)

> 🐲 Once placed on a map, colliders shapes can be edited and moved by directly clicking them ! Don't forget to select the **Move tool** from the tools bar.

![colliders_edit.png](./../media/collision/colliders_edit.png)

