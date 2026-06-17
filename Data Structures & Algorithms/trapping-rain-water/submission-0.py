class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_height = [0]
        max_right_height = [0]
        max_height = 0
        for point_height in height[:-1]:
            max_height = max(max_height, point_height)
            max_left_height.append(max_height)
        max_height = 0
        for point_height in reversed(height[1:]):
            max_height = max(max_height, point_height)
            max_right_height.append(max_height)
        max_right_height = max_right_height[::-1]
        ans = 0
        for i in range(len(height)):
            ans += max(0,min(max_left_height[i], max_right_height[i]) - height[i])
        return ans
