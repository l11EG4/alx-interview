#!/usr/bin/python3
# Made by MEGA
"""here for Defines Island perimeter finding function."""


def island_perimeter(grid):
    """for return the perimiter of an island.
    The grid Represents water by 0 and land by 1.
    Args:
        grid (list): for A list of list of integers representing an island.
    Returns:
        for The Perimeterof the island defined in grid.
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edges += 1
    return size * 4 - edges * 2
