class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [None]*len(nums)
        def jump(start: int):
            if start >= len(nums)-1:
                return True
            if dp[start] is not None:
                return dp[start]
            for i in range(nums[start],0,-1):
                if jump(start+i):
                    dp[start] = True
                    return True
            dp[start] = False
            return False
        return jump(0)