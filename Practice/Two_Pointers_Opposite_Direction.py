#-- Function find_pair_with_sum. --#
def find_pair_with_sum(arr, target):
    left = 0 #-- Initialize left pointer at the begginning of the array on left side. --#
    right = len(arr) - 1 #-- Initialize right pointer at the end of the array on right side. --#
    while left < right: #-- Loop until the left pointer is less than the right pointer. --#
        current_sum = arr[left] + arr[right] #-- Calculate the sum of the elements at the left and right pointers. --#
        if current_sum == target: #-- If the current sum is equal to the target, return the pair. --#
            return (arr[left], arr[right])
        elif current_sum < target: #-- If the current sum is less than the target, move the left pointer to the right. --#
            left += 1
        else: #-- If the current sum is greater than the target, move the right pointer to the left. --#
            right -= 1
#-- Main and Test Cases. --#
if __name__ == "__main__":
    #-- Test Case 1. --#
    arr = [1, 2, 3, 4, 6]
    target = 6
    result = find_pair_with_sum(arr, target)
    if result:
        print(f"Pair found: {result}")
    else:
        print("No pair found.")
    #-- Test Case 2. --#
    arr = [2, 5, 9, 11]
    target = 11
    result = find_pair_with_sum(arr, target)
    if result:
        print(f"Pair found: {result}")
    else:
        print("No pair found.")