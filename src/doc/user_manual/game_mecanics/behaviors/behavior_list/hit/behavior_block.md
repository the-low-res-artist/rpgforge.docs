# ![behavior_icon.png](../../../../../../../media/user_manual/game_mecanics/behaviors/icons/Block.png) Block Behavior
This section covers the RPG Power Forge feature Behavior : Block !

```admonish success title="Oh yeah"
This section is up-to-date !
```

## Summary

## Behavior definition
```admonish summary title="Block Behavior"
The Block Behavior enable the Actor to block an incomming attack / projectile.
```

## Behavior categorie
The Block Behavior is under the Hit Behavior category.

## Behavior sections

### Condition
{{ #include ./../common/condition.md }}

### Parameters
{{ #include ./../common/parameter.md }}

#### Type
{{ #include ./../common/type.md }}

#### Hit
Parameter | Type | Dimension | Definition
---|---|---|---
Stop duration|Number|second|How much the Actor stops when blocking
Repulsion resist|Number|unit|How much the Actor resists the Repulsion (if any)
#### Range
Parameter | Type | Dimension | Definition
---|---|---|---
Angle Opening|Number|Degree| Restrain the blocking to an cone (360 Degree if not provided)
Angle Offset|Number|Degree| Rotate the cone (is provided)

### Animations
{{ #include ./../common/animation.md }}

Here is the list of the available Animations for the current Behavior :

Parameter |Definition
---|---
Hit|Animation played when the Actor is blocking