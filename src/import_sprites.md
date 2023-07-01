# Import a spritesheet

This section covers the import of a spritesheet into **RPG Power Forge** as well as the creation of animations.

> 🐞 [Bug tracker here](https://trello.com/b/PIzgsYov/rpg-power-forge-road-map)

---
## Import Assets UI

To import a spritesheet, you need to access the **Import Assets** User Interface (UI). It is located under the **RPG Power Forge** menu.

![import_button.png](./../media/import/import_button.png)

The UI let you choose what kind of assets you want to import.

![import_ui.png](./../media/import/import_ui.PNG)

---
## Import Animations

You can import a spritesheet to convert it into a **Unity** animation file directly. For instance, let's say I want to import this spritesheet (a set of 8 characters walking in 4 directions, RPG Maker MZ convention):

![spitesheet.png](./../media/import/spritesheet.png)

To do so, select [Animations]

![import_select_animations.png](./../media/import/import_select_animations.PNG)

Then [Sprite Sheet]

![import_select_spritesheet.png](./../media/import/import_select_spritesheet.PNG)

The explorer opens, asking you to select the file itself. Here we will select the spritesheet.png shown above. Once selected, the spritesheet is loaded in the UI.

![import_properties_spritesheet.png](./../media/import/import_properties_spritesheet.PNG)

The following properties do not need to be edited and will be automatically updated after the slice.

Property|Type|Function|Example
--------|--------|--------|--------
Name|String|Name of the selected sprite| sprite_001
Position|Integer|X and Y positions (in pixel) of the selected sprite on the spritesheet|[0;0]
Size|Integer|X and Y sizes (in pixel) of the selected sprite on the spritesheet|[16;20]
Pivot|Selector|Pivot position on the selected sprite (fast selection)|bottom-center
Pivot Offset|Integer|Pivot offset on the selected sprite (pixel selection)|[0;0]

---
## Slice

![import_slice_spritesheet.png](./../media/import/import_slice_spritesheet.PNG)

Select [Slice] to be able to slice your spritesheet according to the following properties.

Property|Type|Function|Example
--------|--------|--------|--------
Method|Enum|Slice method (Pixel Size or Column & Rows numbers)| Pixel Size
Pixel Size|Integer|X and Y sizes (in pixel) of a single sprite on the spritesheet|[16;20]
Row & Column |Integer|number of rows and columns of sprites on the spritesheet|[12;8]
Pivot|Selector|Pivot position on the sprite(s) (fast selection)|bottom-center
Pivot Offset|Integer|Pivot offset on the sprite(s) (pixel selection)|[0;0]

---
## Set Transparent Colors

*In developpement*

---
## Remove Empty Sprites

This action detects empty sprites (with only transparent pixels) and removes them before the sprites are loaded in **RPG Power Forge**.

---
## Other actions

At any time you can always select an individual sprite, or hold SHIFT key for multiple selection. Then right-click to access the sub-menu : Merge or Delete.

![import_delete_spritesheet.png](./../media/import/import_delete_spritesheet.PNG)

### Merge

Merge 2 (or more) sprites together to make 1 sprite.

### Delete

Delete the selected sprite(s). The deleted sprites are not loaded in **RPG Power Forge**.

---
## Apply the slice

Once you are OK, press [Apply] to validate your setup. Your spritesheet will be located in *Assets/Project/Sprites* folder.

![import_apply_spritesheet.png](./../media/import/import_apply_spritesheet.PNG)

---
## Create animations

The next UI allows you to create animations from all of the sprites you have previously sliced.

![import_animation.png](./../media/import/import_animation.PNG)

You can move sprites freely (like cards) to rearange them as you like. WIth right-click on a sprite you can also :
* FlipX
* FlipY
* Delete

### Create an animation with a template
If you are importing a spritesheet that respects an RPG Maker convention. You can use one of our templates to generate all of the animations at once.

![import_select_template.png](./../media/import/import_select_template.png)

*Tadaaa !* The template have been applied. All of the animations have been created correctly.

![import_result_template.png](./../media/import/import_result_template.png)

Below the available templates :

RM|Convention|Details
--------|--------|--------
2000-2003|Character| 4 x 2 characters spritesheet
2000-2003|Vertical| 4 x 2 item spritesheet (4 vertical frames)
2000-2003|Horizontal| 4 x 2 item spritesheet (3 horizontal frames)
XP|Character| 1 character spritesheet
XP|Vertical| 1 item spritesheet (4 vertical frames)
XP|Horizontal| 1 item spritesheet (3 horizontal frames)
VX/MV/MZ|Character| 4 x 2 characters spritesheet
VX/MV/MZ|Vertical| 4 x 2 item spritesheet (4 vertical frames)
VX/MV/MZ|Horizontal| 4 x 2 item spritesheet (3 horizontal frames)

> 🐲 Templates are super useful !

---
### Create your own template

*In developpement*

---
### Create an animation manually

Select at least 2 neightboor sprites thanks to the SHIFT key and right-click.

![import_animation_create.png](./../media/import/import_animation_create.PNG)

Once created, the animation can be selected, renamed, edited and preview-run with the [Play] button.

![import_animation_created.png](./../media/import/import_animation_created.PNG)

Property|Type|Function|Example
--------|--------|--------|--------
Animation Name|String|Name of the animation you are creating|animation_01
Frame Rate|Integer|How fast the animation will run|8

---
## Apply the animations

Once you are OK, press [Apply] to generate all of the animation you have created.

You can rename the animations if you are using a template.

![import_save_result.png](./../media/import/import_save_result.png)

Your animations will be located in *Assets/Project/Animations* folder, grouped under an **Animation Collection**.

![import_animation_collection_location.png](./../media/import/import_animation_collection_location.png)

> 🐲 This is an **Animation Collection**. Double-click this object in your Project window to edit your animations if necessary !
