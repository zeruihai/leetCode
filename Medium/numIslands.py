class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    print("-------------")
                    self.dfs(i,j,grid)
                    count +=1

        return count

                    
    def dfs(self,i,j,grid):
        grid[i][j] = "0"
        for dl, dr in (-1,0),(0,-1),(0,1),(1,0):
            l=i+dl
            r=j+dr
            if 0<=l<len(grid) and 0<=r<len(grid[0]) and grid[l][r]=="1":
                print(l,r)
                self.dfs(l,r,grid)