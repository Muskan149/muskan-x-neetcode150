class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # given a list of nums
        # replace num[i] with 
        
        # leftProds[i] = product of all nums until but excluding i
        # rightProds[i] = product of all nums[-1], nums[-2], ... , nums[i + 1]

        leftProds = []
        rightProds = [0 for _ in range(len(nums))]

        leftProd = rightProd = 1

        leftProds.append(leftProd)
        rightProds[-1] = rightProd

        i = 1
        while i < len(nums):                
            leftProd *= nums[i - 1]
            leftProds.append(leftProd)

            rightProd *= nums[-(i)] # if i = 1, need to only take -1
            rightProds[-(i + 1)] = rightProd # but append to -2

            i += 1
            # print(f"left: {leftProds}")
            # print(f"right: {rightProds}")
        
        res = [rightProds[i] * leftProds[i] for i in range(len(nums))] 

        return res



        
