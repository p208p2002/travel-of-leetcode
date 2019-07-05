class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # print(obstacleGrid)
        # print("")
        try:
            m = len(obstacleGrid[0])
            n = len(obstacleGrid)
        except:
            return 0
        
        if(n == 1 and m == 1 and obstacleGrid[0][0] == 0):
            return 1
        elif(obstacleGrid[0][0] == 1):
            return 0      
        
        # 橫向標記
        for i in range(m):            
            if(i == 0):
                if(obstacleGrid[0][i] == 1):
                    obstacleGrid[0][i] = 0
                else:
                    obstacleGrid[0][i] = 1
            else:
                # 旁邊是障礙物，左邊過不來
                if(obstacleGrid[0][i-1] == 0):
                    obstacleGrid[0][i] = 0
                # 自己是障礙物
                elif(obstacleGrid[0][i] == 1):
                    obstacleGrid[0][i] = 0
                # 自己不是障礙物
                else:                    
                    obstacleGrid[0][i] = 1
        
        #縱向標記
        for i in range(n):
            if(i == 0):
                continue
            
            # 上面是障礙物過不來
            if(obstacleGrid[i-1][0] == 0):
                obstacleGrid[i][0] = 0
            # 自己是障礙物
            elif(obstacleGrid[i][0] == 1):
                obstacleGrid[i][0] = 0
            # 自己不是障礙物
            else:                    
                obstacleGrid[i][0] = 1
            
        # print(obstacleGrid)
        
        # 走剩餘格
        for i in range(n):
            if(i == 0):
                continue
            for j in range(m):
                if(j == 0):
                    continue
                if(obstacleGrid[i][j] == 1):
                    obstacleGrid[i][j] = 0
                else:
                    up = obstacleGrid[i-1][j]
                    left = obstacleGrid[i][j-1]
                    obstacleGrid[i][j] = up + left
        
        #
        return obstacleGrid[n-1][m-1]