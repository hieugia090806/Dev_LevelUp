#-- class Solution. --#
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 
        for i, num in enumerate(nums):
            complement = target - num  
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
#-- If __name__ == "__main__": --#
if __name__ == "__main__":
    #-- Test Case 1. --#
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")
    
    #-- Test Case 2. --#
    nums = [3, 2, 4]
    target = 6
    result = solution.twoSum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")
    
    #-- Test Case 3. --#
    nums = [3, 3]
    target = 6
    result = solution.twoSum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")