# Requirements 
This section list each ?requirement? for RPG Power Forge features as well as their tests results

*(This page is under development)* 

```admonish info title="Testing ..." 
75.0% of tested requirements are passed ✔️ !
```

## Summary

## Context

|Item|Value|
---|---
RPG Power Forge version|0.0.20
Unity Editor version| 2021.3.25f1
Host OS|Windows 10 Family
Host spec|Intel Core i7 2.6GHz (12 cores) 32Go RAM
Date|Dec 14 2023 16:11

## Tests results

Feature|Passed ✔️|Failed ❌|Not tested 💀
---|---|---|---
Assets Importer|3|1|21
Assets Picker|0|0|7
Assets Bar|0|0|7
Tool Bar|0|0|19


## Requirements details

### Assets Importer feature
Requirement|Description|Test result
---|---|---
FORGE_0001|The Assets Importer can import files to make Unity tiles|PASS
FORGE_0002|The Assets Importer can import files to make Unity prefabs|PASS
FORGE_0004|The Assets Importer assemble tiles under a Tiles Collection file|FAIL
FORGE_0005|The Assets Importer assemble props under a Props Collection file|NOT_TESTED
FORGE_0006|The Assets Importer assemble animations under an Animations Collection file|PASS
FORGE_0007|The Assets Importer create the Tiles Collection file at the end of the Tile import process|NOT_TESTED
FORGE_0008|The Assets Importer create the Props Collection file at the end of the Props import process|NOT_TESTED
FORGE_0009|The Assets Importer create the Animations Collection file at the end of the Animation import process|NOT_TESTED
FORGE_0010|The user can import .png file format|NOT_TESTED
FORGE_0011|The user can import .jpeg file format|NOT_TESTED
FORGE_0012|The user can import .bmp file format|NOT_TESTED
FORGE_0013|The user can import .ase file format|NOT_TESTED
FORGE_0014|The user can import .aseprite file format|NOT_TESTED
FORGE_0015|The user can import file or directory of files|NOT_TESTED
FORGE_0016|The user can import file size from 1x1 up to 2048x2048|NOT_TESTED
FORGE_0017|The user can slice the file|NOT_TESTED
FORGE_0018|The user can use premade templates to slice file|NOT_TESTED
FORGE_0019|The user can select a transparency color for the file|NOT_TESTED
FORGE_0020|The user can select a semi-transparency color for the file|NOT_TESTED
FORGE_0021|The user can delete empty sprites|NOT_TESTED
FORGE_0022|The user can choose a collider for a sprite|NOT_TESTED
FORGE_0023|The user can rename sprites|NOT_TESTED
FORGE_0024|The user can reposition sprites|NOT_TESTED
FORGE_0025|The user can cancel the import process|NOT_TESTED
FORGE_0026|The user can edit any collection file after the initial import|NOT_TESTED
### Assets Picker feature
Requirement|Description|Test result
---|---|---
FORGE_0101|The user can view, select, edit and drop on Scene tiles from any �Tiles collection�|NOT_TESTED
FORGE_0102|The user can view, select, edit and drop on Scene props from any �Props collection�|NOT_TESTED
FORGE_0103|The user can view, select, edit and drop on Scene custom colliders|NOT_TESTED
FORGE_0104|The Assets Picker must display assets by category (Actor, Animations, Props, Tiles, Built-In)|NOT_TESTED
FORGE_0105|The Assets Picker must display assets, in each category, by collection|NOT_TESTED
FORGE_0106|The Assets Picker must display a warning is the asset can not be place on the Scene|NOT_TESTED
FORGE_0107|The user can access the Assets Importer directly from the Assets Picker|NOT_TESTED
### Assets Bar feature
Requirement|Description|Test result
---|---|---
FORGE_0201|The Assets Bar must be display at the bottom of the Assets Picker window|NOT_TESTED
FORGE_0202|The Assets Bar must be display at the bottom of the Assets Importer window|NOT_TESTED
FORGE_0203|The Assets Bar must be display at the bottom of each Collection window (Tiles, Props, Animations, ...)|NOT_TESTED
FORGE_0204|The user can zoom-in and zoom-out the assets preview|NOT_TESTED
FORGE_0205|The user can reset the zoom|NOT_TESTED
FORGE_0206|The user can change the background color for the assets preview|NOT_TESTED
FORGE_0207|The user can reset the background color|NOT_TESTED
### Tool Bar feature
Requirement|Description|Test result
---|---|---
FORGE_0301|The Tool Bar is integrated in the Unity Editor|NOT_TESTED
FORGE_0302|The user can undo an action|NOT_TESTED
FORGE_0303|The user can redo an action|NOT_TESTED
FORGE_0304|The user can access the action history|NOT_TESTED
FORGE_0305|The user can create Actors|NOT_TESTED
FORGE_0306|The user can access the Assets Picker|NOT_TESTED
FORGE_0307|The user can access the Assets Properties|NOT_TESTED
FORGE_0308|The user can access the Actors Statistics|NOT_TESTED
FORGE_0309|The user can access the Actors Behaviors|NOT_TESTED
FORGE_0310|The user can toggle the Scene Markers as well as choosing the color|NOT_TESTED
FORGE_0311|The user can access the Unity Play button|NOT_TESTED
FORGE_0312|The user can access the Test Controller|NOT_TESTED
FORGE_0313|The user can access the World Map|NOT_TESTED
FORGE_0314|The user can access the Database|NOT_TESTED
FORGE_0315|The user can access the Settings|NOT_TESTED
FORGE_0316|The user can access the Translation|NOT_TESTED
FORGE_0317|The user can access the Build|NOT_TESTED
FORGE_0318|The user can access the Layout|NOT_TESTED
FORGE_0319|The user can access the Help|NOT_TESTED

