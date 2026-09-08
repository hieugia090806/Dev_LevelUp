def min_subarray_len(arr, k):    
    # Track the minimum length found. Initialize with infinity as a placeholder max value.
    min_length = float('inf')
    # Track the running sum of the elements inside the current window
    current_sum = 0
    # Initialize the left pointer at the start of the array
    left = 0
    
    # The right pointer continuously expands the window to the right, index by index
    for right in range(len(arr)):
        # Add the newly included element to the running sum
        current_sum += arr[right]
        
        # While the current window sum is valid (greater than or equal to k)
        while current_sum >= k:
            # Calculate the current window size (right - left + 1)
            # Update min_length if the current window size is smaller than previous minimums
            min_length = min(min_length, right - left + 1)
            
            # Shrink the window from the left: subtract the leftmost element from the sum
            current_sum -= arr[left]
            # Move the left pointer one step to the right
            left += 1
            
    # If min_length was updated, return it. Otherwise, return 0 (no valid subarray found).
    return min_length if min_length != float('inf') else 0

# Test cases
if __name__ == "__main__":
    # Sample unsorted array input
    nums = [2, 3, 1, 2, 4, 3]
    k_value = 7
    
    # Call the function and store the result
    result = min_subarray_len(nums, k_value)
    
    # Print the output to the console
    print(f"Minimum subarray length with sum >= {k_value} is: {result}")  # Output: 2
