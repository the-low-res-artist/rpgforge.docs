# Behaviors

This section covers the RPG Power Forge feature : Behaviors !

```admonish warning title="Working, working ..."
This section is in work-in-progress
```

## Summary

## Feature definition
```admonish summary title="Behavior"
The Behavior feature gives you the possibility to attach various behaviors to Actors (prefabs). For example, adding the "Attack" behavior to a Player Actor allows them to perform attacks during play.
```

## Feature location

### From the Tool Bar

![window_location2.png](../../../../../../media/user_manual/game_mecanics/behaviors/feature_location_toolbar.png)

## Feature overview

![window_overview.png](../../../../../../media/user_manual/game_mecanics/behaviors/window_overview.png)

The Behavior feature window is splitted in 2 panels :
* left panel : **Tier-list** (list of all attached Behaviors to the current Actor).
* right panel : **Behavior settings** (parameters of the selected Behavior).

## Tier-list

The Tier-list displays every Behaviors attached to the Actor. This list is composed of one or more Tiers : a tier has a color and represents a sub-list of Behavior.

Our sample screenshot contains :
 * a Tier-list composed of 4 Tiers (Red, Yellow, Green and Blue)
 * \+ and \- buttons to add and remove Tiers.

![behavior_list_tiers.png](../../../../../../media/user_manual/game_mecanics/behaviors/behavior_list_tiers.png)

### The role of the Tier-list

The Tier-list is used **to order Behaviors** by priority of activation. A Behavior is activated if its Condition is met (checked every frame).

If a Behavior is in a **warmer Tier** (reddish color) than another one in a **colder Tier** (blueish color), the warmer one will be checked first for its Condition.

If 2 Behaviors are in the same Tier, then the left one will be checked first.

Therefore, to schematize the ordering :
![tier_list_order_check.png](../../../../../../media/user_manual/game_mecanics/behaviors/tier_list_order_check.png)

#### Blocking Behaviors

A **Blocking Behavior** will prevent the activation of the colder ones when  activated (condition is met) until completion :

![behavior_list_tiers.png](../../../../../../media/user_manual/game_mecanics/behaviors/explanation_block_behaviors.gif)

#### Non-Blocking Behaviors

A **non-Blocking Behavior** will allow the activation of the colder ones even when activated (condition is met) :

![behavior_list_tiers.png](../../../../../../media/user_manual/game_mecanics/behaviors/explanation_non_block_behaviors.gif)

## Customization 

### Add a new Behavior

From the Tier-list you can [[Select one of the Green + button]] to add a new Behavior on the corresponding Tier :

![behavior_list_add_behavior.png](../../../../../../media/user_manual/game_mecanics/behaviors/behavior_list_add_behavior.png)

You'll find Behaviors sorted in categories so you can easily find them. You can also use the Search field to filter by name :

![add_new_behavior.gif](../../../../../../media/user_manual/game_mecanics/behaviors/add_new_behavior.gif)

### Customize a Behavior

You can change the name and main color of a Behavior if needed :

![customize_behavior_name.gif](../../../../../../media/user_manual/game_mecanics/behaviors/customize_behavior_name.gif)

### Enable / disable a Behavior

### Move / Remove a Behavior