from leetcode.p0200_number_of_islands import solution


def test_all_water():
    grid = [
        ["0", "0", "0"],
        ["0", "0", "0"],
    ]

    assert solution.Solution().numIslands(grid) == 0


def test_single_land_cell():
    assert solution.Solution().numIslands([["1"]]) == 1


def test_connected_land_is_one_island():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    assert solution.Solution().numIslands(grid) == 1


def test_multiple_islands():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    assert solution.Solution().numIslands(grid) == 3


def test_diagonal_land_is_not_connected():
    grid = [
        ["1", "0", "1"],
        ["0", "1", "0"],
        ["1", "0", "1"],
    ]

    assert solution.Solution().numIslands(grid) == 5


def test_single_row_with_multiple_islands():
    grid = [["1", "1", "0", "1", "0", "1", "1"]]

    assert solution.Solution().numIslands(grid) == 3


def test_single_column_is_connected():
    grid = [["1"], ["1"], ["1"], ["1"]]

    assert solution.Solution().numIslands(grid) == 1
