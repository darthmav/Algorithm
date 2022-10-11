# Given an m x n binary matrix grid. An island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in a grid.
# If there is no island, return 0.


def is_safe(row: int, col: int, rows: int, cols: int) -> bool:
    """
    Checking weather coordinate (row,col) is valid or not.

    >>> is_safe(0, 0, 5, 5)
    True

    >>> is_safe(-1,-1, 5, 5)
    False
    """
    return not (row < 0 or col < 0 or row >= rows or col >= cols)


def dfs(
    row: int, col: int, ROWS: int, COLS: int, seen: set, mat: list[list[int]]
) -> int:
    """
    Returns the current area of the island
    >>> dfs(0,0, 8,8,set(), [ \
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], \
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], \
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
    0
    """
    if is_safe(row, col, ROWS, COLS) and (row, col) not in seen and mat[row][col] == 1:
        seen.add((row, col))
        return (
            1
            + dfs(row + 1, col, ROWS, COLS, seen, mat)
            + dfs(row - 1, col, ROWS, COLS, seen, mat)
            + dfs(row, col + 1, ROWS, COLS, seen, mat)
            + dfs(row, col - 1, ROWS, COLS, seen, mat)
        )
    else:
        return 0


def count_max_area(mat: List[List[int]]) -> int:
    """
    Finds the area of all islands and returns the maximum area.

    >>> count_max_area([ \
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], \
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], \
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
    6
    """

    ROWS = len(mat)
    COLS = len(mat[0])
    seen = set()

    max_area = 0
    for row in range(ROWS):
        for col in range(COLS):
            if mat[row][col] == 1 and (row, col) not in seen:
                # Maximizing the area
                max_area = max(max_area, dfs(row, col, ROWS, COLS, seen, mat))
    return max_area


if __name__ == "__main__":
    import doctest

    # Example 1:
    mat = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]

    print(count_max_area(mat))  # Output -> 6

    """
    Explanation:
    We are allowed to move 4-directionally (horizontal or vertical.)
    so the possible
    in a matrix if we are at x and y position the possible moving are

    >> directions = [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]
    also, we need to care of boundary cases as well
    which are x and y can not be smaller than 0 and greater than a number
    of rows and columns respectively.


    Visualization
    mat = [
    [0,0,A,0,0,0,0,B,0,0,0,0,0],
    [0,0,0,0,0,0,0,B,B,B,0,0,0],
    [0,C,C,0,D,0,0,0,0,0,0,0,0],
    [0,C,0,0,D,D,0,0,E,0,E,0,0],
    [0,C,0,0,D,D,0,0,E,E,E,0,0],
    [0,0,0,0,0,0,0,0,0,0,E,0,0],
    [0,0,0,0,0,0,0,F,F,F,0,0,0],
    [0,0,0,0,0,0,0,F,F,0,0,0,0]
    ]

    For visualization, I have defined the connected island with letters
    by observation, we can see that
        A island is of area 1
        B island is of area 4
        C island is of area 4
        D island is of area 5
        E island is of area 6 and
        F island is of area 5

    it has 6 unique islands of mentioned areas
    and the maximum of all of them is 6 so we return 6.
    """

    doctest.testmod()
