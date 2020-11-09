304pacman
===

Time:       2 weeks

Team:       1

Language:   Python


The project
----
Pathfinding is an extremely common problem in video game programming. It’s why we are asking you to create one for the ghosts in Pacman, with the help of the **Dijkstra algorithm**.
You will illustrate the algorithm and note its distance from the ghost in each visited square.

> If the shortest path isn’t the only one, we will execute searches and study the adjacencies in the following order: North, East, South, West.

> Unlike the original game, the maps aren’t circular.

## USAGE:

```
>> ./304pacman [-h | --help]
USAGE
    ./304pacman file c1 c2file
DESCRIPTION
    file    describing the board, using the following characters:
                ‘0’ for an empty square
                ‘1’ for a wall
                ‘F’ for the ghost’s position
                ‘P’ for Pacman’s position
    c1      character to display for a wall
    c2      character to display for an empty space.
```

Author [**Corentin COUTRET-ROZET**](https://github.com/sheiiva)