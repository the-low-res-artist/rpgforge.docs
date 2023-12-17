# Requirements 
This section list each ?requirement? for RPG Power Forge features as well as their tests results.

*(This page is under development)* 

```admonish tip title="Oh yeah" 
All tested requirements passed ✔️ !
```

## Summary

## Context

|Item|Value|
---|---
RPG Power Forge version|0.0.24
Unity Editor version| 2021.3.25f1
Host OS|Windows 10 Family
Host spec|Intel Core i7 2.6GHz (12 cores) 32Go RAM
Date|December 17 2023 13:53

## Tests results

Feature|Passed ✔️|Failed ❌|Not tested yet...
---|---|---|---
General|2|0|0
Assets Importer|0|0|26
Assets Picker|5|0|2
Assets Bar|0|0|7
Tool Bar|0|0|19


## Requirements details

### General feature
Requirement|Description|Test result
---|---|---
FORGE_0001|RPG Power Forge can be imported and installed in Unity Editor|Passed
FORGE_0002|RPG Power Forge create a menu in Unity Editor top bar|Passed
### Assets Importer feature
Requirement|Description|Test result
---|---|---
FORGE_0101|The Assets Importer can import files to make Unity tiles|Not_tested
FORGE_0102|The Assets Importer can import files to make Unity prefabs|Not_tested
FORGE_0103|The Assets Importer can import files to make Unity animation clips|Not_tested
FORGE_0104|The Assets Importer assemble tiles under a Tiles Collection file|Not_tested
FORGE_0105|The Assets Importer assemble props under a Props Collection file|Not_tested
FORGE_0106|The Assets Importer assemble animations under an Animations Collection file|Not_tested
FORGE_0107|The Assets Importer create the Tiles Collection file at the end of the Tile import process|Not_tested
FORGE_0108|The Assets Importer create the Props Collection file at the end of the Props import process|Not_tested
FORGE_0109|The Assets Importer create the Animations Collection file at the end of the Animation import process|Not_tested
FORGE_0110|The user can import .png file format|Not_tested
FORGE_0111|The user can import .jpeg file format|Not_tested
FORGE_0112|The user can import .bmp file format|Not_tested
FORGE_0113|The user can import .ase file format|Not_tested
FORGE_0114|The user can import .aseprite file format|Not_tested
FORGE_0115|The user can import file or directory of files|Not_tested
FORGE_0116|The user can import file size from 1x1 up to 2048x2048|Not_tested
FORGE_0117|The user can slice the file|Not_tested
FORGE_0118|The user can use premade templates to slice file|Not_tested
FORGE_0119|The user can select a transparency color for the file|Not_tested
FORGE_0120|The user can select a semi-transparency color for the file|Not_tested
FORGE_0121|The user can delete empty sprites|Not_tested
FORGE_0122|The user can choose a collider for a sprite|Not_tested
FORGE_0123|The user can rename sprites|Not_tested
FORGE_0124|The user can reposition sprites|Not_tested
FORGE_0125|The user can cancel the import process|Not_tested
FORGE_0126|The user can edit any collection file after the initial import|Not_tested
### Assets Picker feature
Requirement|Description|Test result
---|---|---
FORGE_0201|The user can view, select, edit and drop on Scene tiles from any Tiles collection|Passed
FORGE_0202|The user can view, select, edit and drop on Scene props from any Props collection|Passed
FORGE_0203|The user can view, select, edit and drop on Scene custom colliders|Passed
FORGE_0204|The Assets Picker must display assets by category (Actor, Animations, Props, Tiles, Built-In)|Passed
FORGE_0205|The Assets Picker must display assets, in each category, by collection|Passed
FORGE_0206|The Assets Picker must display a warning is the asset can not be place on the Scene|Not_tested
FORGE_0207|The user can access the Assets Importer directly from the Assets Picker|Not_tested
### Assets Bar feature
Requirement|Description|Test result
---|---|---
FORGE_0301|The Assets Bar must be display at the bottom of the Assets Picker window|Not_tested
FORGE_0302|The Assets Bar must be display at the bottom of the Assets Importer window|Not_tested
FORGE_0303|The Assets Bar must be display at the bottom of each Collection window (Tiles, Props, Animations, ...)|Not_tested
FORGE_0304|The user can zoom-in and zoom-out the assets preview|Not_tested
FORGE_0305|The user can reset the zoom|Not_tested
FORGE_0306|The user can change the background color for the assets preview|Not_tested
FORGE_0307|The user can reset the background color|Not_tested
### Tool Bar feature
Requirement|Description|Test result
---|---|---
FORGE_0401|The Tool Bar is integrated in the Unity Editor|Not_tested
FORGE_0402|The user can undo an action|Not_tested
FORGE_0403|The user can redo an action|Not_tested
FORGE_0404|The user can access the action history|Not_tested
FORGE_0405|The user can create Actors|Not_tested
FORGE_0406|The user can access the Assets Picker|Not_tested
FORGE_0407|The user can access the Assets Properties|Not_tested
FORGE_0408|The user can access the Actors Statistics|Not_tested
FORGE_0409|The user can access the Actors Behaviors|Not_tested
FORGE_0410|The user can toggle the Scene Markers as well as choosing the color|Not_tested
FORGE_0411|The user can access the Unity Play button|Not_tested
FORGE_0412|The user can access the Test Controller|Not_tested
FORGE_0413|The user can access the World Map|Not_tested
FORGE_0414|The user can access the Database|Not_tested
FORGE_0415|The user can access the Settings|Not_tested
FORGE_0416|The user can access the Translation|Not_tested
FORGE_0417|The user can access the Build|Not_tested
FORGE_0418|The user can access the Layout|Not_tested
FORGE_0419|The user can access the Help|Not_tested

