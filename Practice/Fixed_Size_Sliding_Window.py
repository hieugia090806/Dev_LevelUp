#-- Problem: Find the maximum sum of any contiguous subarray of a fixed size $k$.. --#
from typing import List

def max_sub_array_of_size_k(k: int, nums: List[int]) -> int:

    max_sum = 0
    window_sum = 0
    
    # 1. Calculate the sum of the first window of size k
    for i in range(k):
        window_sum += nums[i]
    max_sum = window_sum
    
    # 2. Slide the window to the right
    for right in range(k, len(nums)):
        # Add the new element on the right, subtract the old element on the left
        window_sum = window_sum + nums[right] - nums[right - k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum

if __name__ == "__main__":
    nums = [2, 1, 5, 1, 3, 2]
    k = 3
    print(f"Max sum of size {k}: {max_sub_array_of_size_k(k, nums)}")  # Output: 9 (subarray [5, 1, 3])