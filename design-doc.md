# Design

## Start Interaction

When the game is started, the basic rules of the game will be displayed. the user 

## Entering A Room

Upon entering a room, the room will be described for the player. Based on what items are in the room, actions will take place. If the room has a pit in it, the player will be hurt by 1-20 hit points. If the room has a potion, the player will collect the potion. If a Pillar is in the room the player collects the pillar. Once the room contents has been described, the player is given a list of options, including traversing  through any available doors. After exiting the room, the console output will be reset.

## Dungeon Creation

The dungeon must have an entrance and an exit with a path connecting them. In addition, there needs to be a room containing each of the pillars and there must be a path from the entrance to each of these rooms as well.

The dungeon will be represented as a 2d array of room elements. This allows us to reference them by x-y coordinates and better keep track of the players location and ensure there is an ensured path to all pillars and the exit from the starting position.

## Traversal

If a room has a door in either the North, South, East, or West direction the user can travel in that direction.

## Items

There is a 10% chance that an item will appear in the dungeon. The items are listed below with their properties.

### Health Potion

A health potion allows the player to regain 5-15 health up to 100%.

### Vision Potion

A vision potion allows the player to see what is in up to 8 rooms surrounding them. The bounds of the maze will be represented by ***. This allows them to avoid possible pits in the road or dead ends. It will print out the representation for that room.

### Pillar

The goal of the player is to collect all of the pillars and exit the dungeon. There are four pillars A, E, I and P that represent the 4 pillars of OOP. Once they have been collected, the user can exit the dungeon.
