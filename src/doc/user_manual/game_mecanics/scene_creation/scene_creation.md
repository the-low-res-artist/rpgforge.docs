# Scene Creation

This section covers the RPG Power Forge feature : Scene Creation !

```admonish success title="Oh yeah"
This section is up-to-date !
```

## Summary

## Feature definition
```admonish summary title="Scene Creation"
The Scene Creation feature allows you to create a new Scene in Unity with predefined settings (player spawn point, tilemap, ...)
```

## Feature location

### From the Tool Bar

![window_location2.png](../../../../../../media/user_manual/game_mecanics/scene_creation/location_tool_bar.png)

## Feature details

### New Unity Scene
When you select the "Create Scene" option, a new Unity Scene is created with the following GameObjects :
* **Root** : A parent GameObject for the whole Scene.
  * **Tilemap** : A Tilemap GameObject to draw tiles on it.
  * **Start** : A Spawner GameObject for the Player character. 

![window_location2.png](../../../../../../media/user_manual/game_mecanics/scene_creation/new_scene_setup.png)

### Directly playable

Because the Scene is automatically shipped with a "Start" GameObject, you can press the Play button to directly run the Scene :
![window_location2.png](../../../../../../media/user_manual/game_mecanics/scene_creation/scene_creation_test.gif)