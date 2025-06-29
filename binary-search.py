class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialize left, right, mid
        left, right = 0, len(nums) - 1
        # while left < right:
        # calculate mid
        while left <= right:
            mid = (left + right) // 2
        # if nums.mid > target
            # look left: right = mid - 1
            if nums[mid] > target:
                right = mid - 1 
        # if nums.mid < target
            # look right: left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
        # else return mid
            else:
                return mid
        
        return -1
