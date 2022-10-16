"""
wissamfawaz12@gmail.com | github.com/wissamfawaz
This implementation demonstrates how to generate the
elements of a Pascal's triangle.
What is Pascal's triangle?
- Refer to (https://en.wikipedia.org/wiki/Pascal%27s_triangle)
for more info about this triangle.
"""


def generate_pascal_triangle(num_rows: int) -> None:
    """
    Print Pascal's triangle for different number of rows
    >>> generate_pascal_triangle(1)
    [[1]]
    >>> generate_pascal_triangle(2)
    [[1], [1, 1]]
    >>> generate_pascal_triangle(3)
    [[1], [1, 1], [1, 2, 1]]
    >>> generate_pascal_triangle(4)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    >>> generate_pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    triangle: list[list[int]] = []
    for current_row_idx in range(num_rows):
        populate_current_row(triangle, current_row_idx)
    print(triangle)


def populate_current_row(triangle: list[list[int]], current_row_idx: int) -> None:
    """
    >>> triangle = [[1]]
    >>> populate_current_row(triangle, 1)
    >>> triangle
    [[1], [1, 1]]
    >>> populate_current_row(triangle, 2)
    >>> triangle
    [[1], [1, 1], [1, 2, 1]]
    """
    current_row = [-1] * (current_row_idx + 1)
    # first and last elements of current row are equal to 1
    current_row[0], current_row[-1] = 1, 1
    for current_col_idx in range(1, current_row_idx):
        calculate_current_element(
            triangle, current_row, current_row_idx, current_col_idx
        )
    triangle.append(current_row)


def calculate_current_element(
    triangle: list[list[int]],
    current_row: list[int],
    current_row_idx: int,
    current_col_idx: int,
) -> None:
    """
    >>> triangle = [[1], [1, 1]]
    >>> current_row = [1, -1, 1]
    >>> calculate_current_element(triangle, current_row, 2, 1)
    >>> current_row
    [1, 2, 1]
    """
    above_to_left_elt = triangle[current_row_idx - 1][current_col_idx - 1]
    above_to_right_elt = triangle[current_row_idx - 1][current_col_idx]
    current_row[current_col_idx] = above_to_left_elt + above_to_right_elt


if __name__ == "__main__":
    import doctest

    doctest.testmod()
