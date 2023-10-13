#https://leetcode.com/problems/number-of-islands/
class Solution:
    def island_positions(grid, pos1, pos2):
        ans = []
        xshift = [-1, 0, 0, 1]
        yshift = [0, 1, -1, 0]
        for pos, val in enumerate(yshift):
            if (pos1+val < 0) or (pos1+val > len(grid)) or (pos2 + xshift[pos] < 0) or (pos2 + xshift[pos] > len(grid[pos1])):
                continue
            elif grid[pos1+val][pos2+xshift[pos]] == "1":
                if [pos1+val, pos2+xshift[pos]] not in ans: 
                    ans.append([pos1+val, pos2+xshift[pos]])
        for pos, i in enumerate(ans):
            Solution.island_positions(grid, ans[pos][0], ans[pos][1])
    def numIslands(self, grid):
        ans = 0
        islands = []
        for pos1, row in grid:
            for pos2, value in grid[pos1]:
                if value == "1":
                    islands.append(Solution.island_positions(grid, pos1, pos2))
        
        return ans
