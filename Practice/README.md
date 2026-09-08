# A. Brief Introduction of Technique. #
>
  ## 1.1 Techniques Frequently Used:. ##
    + Prefix Sum 
    + Two Pointers 
    + Sliding Window
    + Binary Search 
    + Greedy 
    + Quy hoạch động 
    + Backtracking
  ## 1.2 Signals for each technique. ##
    + Hỏi tổng của nhiều đoạn con khác nhau -> Prefix Sum
    + Mảng đã sắp, tìm cặp theo tổng -> Two Pointers
    + Đoạn con LIÊN TIẾP tối ưu -> Sliding Window
    + Tìm trong mảng sắp xếp lớn/ngưỡng nhỏ nhất -> Binary Search
    + Mỗi bước chọn 'to nhất' và bài cho phép -> Greedy
    + Đếm số cách/tối ưu, bài con chồng lấp -> Dynamic Programming
    + Liệt kê mọi cấu hình có ràng buộc -> Backtracking
>
# B.Technical Description Detail. #
>
  ## 2.1 Prefix Sum Technical Description. ##
  - Definition: A preprocessing technique that computes and stores the cumulative sum of elements from the beginning of the array up to the current index.
  - Purpose: Optimizes range sum queries for any interval [L, R].
  - Time Complexity:
    + Preprocessing: O(N) - Executed once to build the Prefix Sum array.
    + Query: O(1) - Retrieves the sum of range [L, R] instantly, highly efficient for multiple recurring queries.
  - Formula:
    + P[i] = P[i-1] + A[i]
    + Sum(L, R) = P[R] - P[L-1] (for L > 0)

  ## 2.2 Two Pointer Technique. ##
  - Definition: The **Two Pointer technique** is a highly efficient algorithmic strategy primarily used to optimize problems on linear data structures such as Arrays, Strings, or Linked Lists.Instead of using nested loops that lead to a high time complexity of $O(N^2)$, this technique utilizes two index variables (pointers) that move through the data structure in a synchronized, intelligent manner. This effectively reduces the time complexity down to a linear **$O(N)$**.
  - Type 1: Opposite Direction Pointers
    + **How it works:** Two pointers start at opposite ends of the array (one at index `0` and one at index `N-1` and move toward the center until they meet or cross.
    + **Prerequisite:** Usually requires the input data to be **sorted**.
    + **Common problems:** Finding a pair of numbers that sum up to a target (Two Sum on sorted array), Checking if a string is a palindrome.
  - Type 2: Same Direction Pointers / Sliding Window
    + **How it works:** Both pointers start from the beginning of the array and move towards the end. The leading pointer (`right`) expands the window to look for valid states, while the trailing pointer (`left`) contracts the window once the problem's condition is met.
    + **Common problems:** Longest substring without repeating characters, Minimum size subarray sum $\ge$ K.
  - Type 3: Fast & Slow Pointers (Tortoise and Hare).
    + **How it works:** Both pointers start at the same position but move at different speeds (e.g., the `fast` pointer moves 2 steps per iteration, while the `slow` pointer moves only 1 step).
    + **Common problems:** Detecting a cycle (infinite loop) in a Linked List, Finding the middle element of a Linked List.
  - 📊 Performance Comparison
    + **Brute Force Approach:** Time complexity of **$O(N^2)$** due to nested `for` loops.
    + **Two Pointer Approach:** Time complexity of **$O(N)$** because each element is processed a constant number of times.
    + **Space Complexity:** Typically **$O(1)$** since it only requires a few extra index variables without allocating additional memory arrays.
   
    ## 2. Sliding Window Technique. ##
    A powerful algorithmic technique used to reduce time complexity from $O(n^2)$ to $O(n)$ when processing sequential data (arrays or strings). 
    + **Fixed-size Window:** Maintains a constant window length ($k$) to find sub-metrics (e.g., maximum sum of size $k$).
    + **Dynamic-size Window:** Expands and shrinks the window dynamically using `left` and `right` pointers to satisfy specific conditions (e.g., finding the shortest or longest subarray)
