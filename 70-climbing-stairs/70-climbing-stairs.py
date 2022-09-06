class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1 or n == 2:
        #     return n
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        
        path = {1:1, 2:2, 3:3}
        
        for i in range(4, n+1):
            path[i] = path[i-1] + path[i-2]
            
        print(path)
        return path[n]
      
        