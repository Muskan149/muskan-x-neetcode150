class Solution:
    def maxArea(self, height: List[int]) -> int:
        # initialize left and right
        left, right = 0, len(height) - 1
        maxWater = 0
        # while left < right
        while left < right:
        # right - left is the width
            w = right - left
            # min(height[left], height[right]) is the height
            h = min(height[left], height[right])
            water = w * h
            maxWater = water if water > maxWater else maxWater
            # now explore more: do i move one step left or right:
            # if left + 1 > nums.left -> then left += 1
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
         
        return maxWater


        
