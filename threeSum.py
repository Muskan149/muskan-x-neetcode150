class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array so you can perform 2 sum 2 in O(n) time and O(1) space
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i < len(nums) - 2:
                left, right = i + 1, len(nums) - 1
                while left < right:
                    sum_ = nums[left] + nums[right] + num
                    if sum_ > 0:
                        right -= 1
                    elif sum_ < 0:
                        left += 1
                    else:
                        triplet = [num, nums[left], nums[right]]
                        print(f"found a triplet {triplet}")
                        if triplet not in res:
                            res.append(triplet)
                        left += 1
                        right -= 1
        
        return res


        
