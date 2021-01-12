#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2021/1/12 15:36
# @Author : Snowball

grid = [[1,3,1],[1,5,1],[4,2,1]]
import numpy as np

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #dp = np.mat(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = min(grid[i][j-1],grid[i-1][j]) + grid[i][j]
        return grid[-1][-1]






res = Solution().minPathSum(grid)
print(res)
