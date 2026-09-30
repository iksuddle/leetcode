# 200. Number of Islands


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()

        # dfs until there are no neighboring island cells, marking island cells as seen
        def map_island(row, col):
            # bounds check
            if not 0 <= row < m or not 0 <= col < n:
                return
            # this is not an island or we have already seen it
            if grid[row][col] != "1" or (row, col) in seen:
                return

            seen.add((row, col))

            map_island(row + 1, col)
            map_island(row - 1, col)
            map_island(row, col + 1)
            map_island(row, col - 1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in seen:
                    map_island(i, j)
                    count += 1

        return count
