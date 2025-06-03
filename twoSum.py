class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialize hash map mapping a number to its pos'n
        numToPosition = {}

        # populate hashmap
        for i, num in enumerate(nums):
            numToPosition[num] = i
        
        # try to find the a pair of numbers that add up to the target
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numToPosition and numToPosition[complement] != i:
                return [i, numToPosition[complement]]






        
