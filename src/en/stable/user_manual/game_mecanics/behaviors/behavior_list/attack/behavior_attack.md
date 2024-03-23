# ![behavior_icon.png](../../../../../../../../media/user_manual/game_mecanics/behaviors/icons/Attack.png) Attack Behavior
(<( behavior )><( attack )><( melee )><( weapon )><( sword )><( hammer )><( hit )><( slash )>)
This section covers the RPG Power Forge feature Behavior : Attack !

```admonish warning title="Working, working ..."
This section is in work-in-progress
```

## Summary

## Behavior definition
```admonish summary title="Attack Behavior"
The Attack Behavior enable the Actor to use a melee attack.
```

## Behavior categorie
The Attack Behavior is under the Attack Behavior category (no way).
## Behavior overview

## Behavior sections

### Condition
{{ #include ./../common/condition.md }}

### Parameters
{{ #include ./../common/parameter.md }}

#### Type
{{ #include ./../common/type.md }}

#### Shape
Parameter | Type | Dimension | Definition
---|---|---|---
Shape|Selector| --- |The shape of the attack hitbox
Range|Number|unit|The size of the attack hitbox
#### Direction
Parameter | Type | Dimension | Definition
---|---|---|---
Direction|Selector|---|The direction of the attack
Snap|Checkbox|---|Should attacks follow the exact input direction, or should they align with the Actor's direction (like limited to 4 or 8 directions)
#### Offset
Parameter | Type | Dimension|Definition
---|---|---|---
Angle Offset|Number|Degree|Offset at which the hitbox is rotated
Front Offset|Number|unit|Offset at which the hitbox is translated
Side Offset|Number|unit|Offset at which the hitbox is translated
#### Repulsion
Parameter | Type | Dimension|Definition
---|---|---|---
Repulsion|Number|unit/second²|How much the Actor is pushed backward when attacking
#### Timing
Parameter | Type | Dimension|Definition
---|---|---|---
Prepare Duration|Number|second|How long the Actor is preparing to attack (linked to [Prepare Animation](#{Prepare}))
Attack Duration|Number|second|How long the Actor is attacking (linked to [Attack Animation](#{Attack}))
Stop Duration|Number|second|How long the Actor stops when attacking
Cooldown Duration|Number|second|How long before the Actor can attack again
#### Character Stop
Parameter | Type | Dimension|Definition
---|---|---|---
Stop Mode|Selector|---|How the Actor should stop during the attack
Stop Deceleration|Number|unit/second²|How brutal is the stop when the Actor is attacking
Forward Impulse|Number|unit/second²|How much the Actor is pushed forward when attacking
#### Repulsion
Parameter | Type | Dimension|Definition
---|---|---|---
Backward Impulse|Number|unit/second²|How much the Actor is pushed backward when the attack is being blocked
### Animations
{{ #include ./../common/animation.md }}
Parameter |Definition
---|---
Prepare|Animation before the actual attack (if any)
Attack|Attack animation