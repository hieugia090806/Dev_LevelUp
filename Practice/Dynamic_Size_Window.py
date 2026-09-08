#-- Problem: Find the minimal length of a contiguous subarray of which the sum is greater than or equal to a given target. --#
from typing import List

def min_sub_array_len(target: int, nums: List[int]) -> int:
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        # 1. Expand the window by adding the right element
        current_sum += nums[right]
        
        # 2. Shrink the window from the left as long as the condition (>= target) is met
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1  # Move the left pointer to narrow the window
            
    return min_length if min_length != float('inf') else 0

if __name__ == "__main__":
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(f"Minimal length: {min_sub_array_len(target, nums)}")  # Output: 2 (subarray [4, 3])